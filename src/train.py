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


def estimate_loss(model: GPTLanguageModel, val_loader, device: str) -> float:
    model.eval()
    total_loss = 0.0
    total_count = 0
    with torch.no_grad():
        for xb, yb in val_loader:
            xb, yb = xb.to(device), yb.to(device)
            logits = model(xb)
            loss = F.cross_entropy(logits.view(-1, logits.size(-1)), yb.view(-1))
            total_loss += loss.item() * xb.size(0)
            total_count += xb.size(0)
    return total_loss / total_count


def train(config: GPTConfig) -> None:
    set_seed(config.seed)
    train_loader, val_loader, stoi, itos = load_data(
        config.data_path,
        config.block_size,
        config.batch_size,
        val_ratio=config.val_ratio,
    )

    model = GPTLanguageModel(
        vocab_size=len(stoi),
        block_size=config.block_size,
        emb_dim=config.n_embd,
        num_heads=config.n_head,
        num_layers=config.n_layer,
        dropout=config.dropout,
    ).to(config.device)

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
            if step % config.eval_interval == 0 or step == config.max_iters:
                val_loss = estimate_loss(model, val_loader, config.device)
                elapsed = time.time() - start_time
                print(f"step {step:5d} | train loss {loss.item():.4f} | val loss {val_loss:.4f} | elapsed {elapsed:.1f}s")
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
                print(f"saved checkpoint: {checkpoint_path}")

            if step >= config.max_iters:
                break

    print("Training complete.")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Train Tiny GPT")
    parser.add_argument("--data_path", type=str, default="data/input.txt")
    parser.add_argument("--output_dir", type=str, default="checkpoints")
    parser.add_argument("--block_size", type=int, default=64)
    parser.add_argument("--batch_size", type=int, default=64)
    parser.add_argument("--max_iters", type=int, default=2000)
    parser.add_argument("--eval_interval", type=int, default=500)
    parser.add_argument("--learning_rate", type=float, default=3e-4)
    parser.add_argument("--n_embd", type=int, default=128)
    parser.add_argument("--n_head", type=int, default=4)
    parser.add_argument("--n_layer", type=int, default=4)
    parser.add_argument("--dropout", type=float, default=0.1)
    parser.add_argument("--val_ratio", type=float, default=0.1)
    parser.add_argument("--seed", type=int, default=42)
    return parser.parse_args()


if __name__ == "__main__":
    args = parse_args()
    config = GPTConfig(
        data_path=args.data_path,
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
