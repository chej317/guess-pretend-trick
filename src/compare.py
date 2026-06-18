import argparse
import os
import torch
import json
from src.dataset import decode_text
from src.model import GPTLanguageModel

def generate_from_checkpoint(checkpoint_path, prompt, max_new_tokens, device):
    if not os.path.exists(checkpoint_path):
        return f"Error: Checkpoint {checkpoint_path} not found."
    
    checkpoint = torch.load(checkpoint_path, map_location=device)
    config = checkpoint["config"]
    stoi = checkpoint["stoi"]
    itos = checkpoint["itos"]

    model = GPTLanguageModel(
        vocab_size=len(stoi),
        block_size=config["block_size"],
        emb_dim=config["n_embd"],
        num_heads=config["n_head"],
        num_layers=config["n_layer"],
        dropout=config["dropout"],
    ).to(device)
    model.load_state_dict(checkpoint["model_state_dict"])
    model.eval()

    context = [stoi.get(ch, 0) for ch in prompt[-config["block_size"] :]]
    context_tensor = torch.tensor([context], dtype=torch.long, device=device)

    with torch.no_grad():
        output = model.generate(
            context_tensor,
            max_new_tokens=max_new_tokens,
            temperature=1.0,
            top_k=None,
        )

    return decode_text(output[0], itos)

def main():
    parser = argparse.ArgumentParser(description="Compare multiple GPT checkpoints")
    parser.add_argument("--steps", type=int, nargs="+", required=True, help="List of step numbers to compare")
    parser.add_argument("--dir", type=str, default="checkpoints", help="Directory where checkpoints are stored")
    parser.add_argument("--prompt", type=str, default="Once upon a time,", help="Prompt for generation")
    parser.add_argument("--tokens", type=int, default=100, help="Number of tokens to generate")
    args = parser.parse_args()

    device = "cuda" if torch.cuda.is_available() else "cpu"
    print(f"Comparing checkpoints with prompt: '{args.prompt}'\n")

    results = []
    for step in args.steps:
        path = os.path.join(args.dir, f"gpt_checkpoint_{step}.pt")
        print(f"Generating from Step {step}...", end="", flush=True)
        text = generate_from_checkpoint(path, args.prompt, args.tokens, device)
        print(" Done.")
        results.append({"step": step, "text": text})

    print("\n" + "="*50)
    print("EVOLUTION OF INTELLIGENCE REPORT")
    print("="*50 + "\n")

    for res in results:
        print(f"--- STEP {res['step']} ---")
        print(res['text'])
        print("\n")

if __name__ == "__main__":
    main()
