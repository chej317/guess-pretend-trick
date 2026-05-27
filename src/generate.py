import argparse
import torch

from src.dataset import decode_text
from src.model import GPTLanguageModel


def load_checkpoint(path: str, device: str):
    checkpoint = torch.load(path, map_location=device)
    return checkpoint


def main() -> None:
    parser = argparse.ArgumentParser(description="Generate text from a trained GPT checkpoint")
    parser.add_argument("--checkpoint", type=str, required=True)
    parser.add_argument("--start_text", type=str, default="ROMEO:")
    parser.add_argument("--max_new_tokens", type=int, default=300)
    parser.add_argument("--temperature", type=float, default=1.0)
    parser.add_argument("--top_k", type=int, default=None)
    parser.add_argument("--device", type=str, default="cuda" if torch.cuda.is_available() else "cpu")
    args = parser.parse_args()

    device = args.device
    checkpoint = load_checkpoint(args.checkpoint, device)
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

    context = [stoi.get(ch, 0) for ch in args.start_text[-config["block_size"] :]]
    context_tensor = torch.tensor([context], dtype=torch.long, device=device)

    with torch.no_grad():
        output = model.generate(
            context_tensor,
            max_new_tokens=args.max_new_tokens,
            temperature=args.temperature,
            top_k=args.top_k,
        )

    print(decode_text(output[0], itos))


if __name__ == "__main__":
    main()
