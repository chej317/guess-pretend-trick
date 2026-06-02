import argparse
import os
import random
import time

import torch
import torch.nn.functional as F
from torch.optim import AdamW

from src.config import GPTConfig
from src.dataset import load_data
from src.model import GPTLanguageModel


def set_seed(seed: int) -> None:
    random.seed(seed)
    torch.manual_seed(seed)
    if torch.cuda.is_available():
        torch.cuda.manual_seed_all(seed)


def estimate_loss(model: GPTLanguageModel, val_loader, device: str, eval_iters: int = 100) -> float:
    model.eval()
    total_loss = 0.0
    total_count = 0
    with torch.no_grad():
        for i, (xb, yb) in enumerate(val_loader):
            if i >= eval_iters:
                break
            xb, yb = xb.to(device), yb.to(device)
            logits = model(xb)
            loss = F.cross_entropy(logits.view(-1, logits.size(-1)), yb.view(-1))
            total_loss += loss.item() * xb.size(0)
            total_count += xb.size(0)
    return total_loss / total_count


def train(config: GPTConfig) -> None:
    # ... (rest of the setup code remains same)
    set_seed(config.seed)
    train_loader, val_loader, stoi, itos = load_data(
        config.data_path,
        config.block_size,
        config.batch_size,
        val_ratio=config.val_ratio,
        is_hf=config.is_hf,
        sample_size=config.sample_size,
    )

    vocab_size = len(stoi)
    model = GPTLanguageModel(
        vocab_size=vocab_size,
        block_size=config.block_size,
        emb_dim=config.n_embd,
        num_heads=config.n_head,
        num_layers=config.n_layer,
        dropout=config.dropout,
    ).to(config.device)

    # Calculate model size
    n_params = sum(p.numel() for p in model.parameters())
    
    print("-" * 30)
    print("🚀 Training Summary")
    print(f"• Dataset: {config.data_path} ({'HuggingFace' if config.is_hf else 'Local'})")
    print(f"• Vocab Size: {vocab_size}")
    print(f"• Batch Size: {config.batch_size}")
    print(f"• Block Size: {config.block_size}")
    print(f"• Model Size: {n_params:,} parameters")
    print(f"• Device: {config.device}")
    print(f"• Max Iters: {config.max_iters}")
    print("-" * 30)

    optimizer = AdamW(model.parameters(), lr=config.learning_rate)
    os.makedirs(config.output_dir, exist_ok=True)
    step = 0
    start_time = time.time()

    while step < config.max_iters:
        model.train()
        for xb, yb in train_loader:
            xb, yb = xb.to(config.device), yb.to(config.device)
            logits = model(xb)
            loss = F.cross_entropy(logits.view(-1, logits.size(-1)), yb.view(-1))
            optimizer.zero_grad()
            loss.backward()
            optimizer.step()

            step += 1
            
            # Regular progress update
            if step % 100 == 0:
                print(f"Step {step:5d}/{config.max_iters} | Loss: {loss.item():.4f}", end="\r")

            # Evaluation and Checkpoint
            if step % config.eval_interval == 0 or step == config.max_iters:
                print(f"\n🔍 Step {step}: Starting evaluation...", end="", flush=True)
                val_loss = estimate_loss(model, val_loader, config.device, config.eval_iters)
                elapsed = time.time() - start_time
                print(f"\r✅ Step {step:5d} | Train Loss: {loss.item():.4f} | Val Loss: {val_loss:.4f} | Time: {elapsed:.1f}s")
                
                print(f"💾 Saving checkpoint to {config.output_dir}...", end="", flush=True)
                checkpoint_path = os.path.join(config.output_dir, f"gpt_checkpoint_{step}.pt")
                torch.save(
                    {
                        "model_state_dict": model.state_dict(),
                        "config": config.__dict__,
                        "stoi": stoi,
                        "itos": itos,
                    },
                    checkpoint_path,
                )
                print(f"\r💾 Saved checkpoint: {checkpoint_path}          ")

            if step >= config.max_iters:
                break

    print("Training complete.")


def parse_args() -> argparse.Namespace:
    default_config = GPTConfig()
    parser = argparse.ArgumentParser(description="Train Tiny GPT")
    parser.add_argument("--data_path", type=str, default=default_config.data_path)
    
    # HF dataset toggle
    hf_group = parser.add_mutually_exclusive_group()
    hf_group.add_argument("--is_hf", action="store_true", dest="is_hf", help="Use Hugging Face dataset")
    hf_group.add_argument("--no_hf", action="store_false", dest="is_hf", help="Use local file instead of HF")
    parser.set_defaults(is_hf=default_config.is_hf)

    parser.add_argument("--sample_size", type=int, default=default_config.sample_size)
    parser.add_argument("--output_dir", type=str, default=default_config.output_dir)
    parser.add_argument("--block_size", type=int, default=default_config.block_size)
    parser.add_argument("--batch_size", type=int, default=default_config.batch_size)
    parser.add_argument("--max_iters", type=int, default=default_config.max_iters)
    parser.add_argument("--eval_interval", type=int, default=default_config.eval_interval)
    parser.add_argument("--learning_rate", type=float, default=default_config.learning_rate)
    parser.add_argument("--n_embd", type=int, default=default_config.n_embd)
    parser.add_argument("--n_head", type=int, default=default_config.n_head)
    parser.add_argument("--n_layer", type=int, default=default_config.n_layer)
    parser.add_argument("--dropout", type=float, default=default_config.dropout)
    parser.add_argument("--val_ratio", type=float, default=default_config.val_ratio)
    parser.add_argument("--seed", type=int, default=default_config.seed)
    return parser.parse_args()


if __name__ == "__main__":
    args = parse_args()
    config = GPTConfig(
        data_path=args.data_path,
        is_hf=args.is_hf,
        sample_size=args.sample_size,
        block_size=args.block_size,
        batch_size=args.batch_size,
        max_iters=args.max_iters,
        eval_interval=args.eval_interval,
        learning_rate=args.learning_rate,
        n_embd=args.n_embd,
        n_head=args.n_head,
        n_layer=args.n_layer,
        dropout=args.dropout,
        val_ratio=args.val_ratio,
        seed=args.seed,
        output_dir=args.output_dir,
    )
    train(config)
