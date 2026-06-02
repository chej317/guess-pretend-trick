from pathlib import Path
from typing import Dict, Tuple, Optional

import torch
from torch.utils.data import Dataset, DataLoader
from datasets import load_dataset


class NextTokenDataset(Dataset):
    def __init__(self, data: torch.Tensor, block_size: int):
        self.data = data
        self.block_size = block_size

    def __len__(self) -> int:
        return len(self.data) - self.block_size

    def __getitem__(self, idx: int) -> Tuple[torch.Tensor, torch.Tensor]:
        x = self.data[idx : idx + self.block_size]
        y = self.data[idx + 1 : idx + self.block_size + 1]
        return x, y


def build_vocabulary(text: str) -> Tuple[Dict[str, int], Dict[int, str]]:
    chars = sorted(set(text))
    stoi = {ch: i for i, ch in enumerate(chars)}
    itos = {i: ch for ch, i in stoi.items()}
    return stoi, itos


def encode_text(text: str, stoi: Dict[str, int]) -> torch.Tensor:
    return torch.tensor([stoi[ch] for ch in text], dtype=torch.long)


def decode_text(tokens: torch.Tensor, itos: Dict[int, str]) -> str:
    return "".join(itos[int(i)] for i in tokens)


def load_data(
    data_path: str,
    block_size: int,
    batch_size: int,
    val_ratio: float = 0.1,
    is_hf: bool = False,
    sample_size: Optional[int] = None,
) -> Tuple[DataLoader, DataLoader, Dict[str, int], Dict[int, str]]:
    if is_hf:
        print(f"Loading dataset '{data_path}' from Hugging Face...")
        dataset = load_dataset(data_path, split="train", trust_remote_code=True)
        if sample_size and sample_size < len(dataset):
            print(f"Sampling {sample_size} examples...")
            dataset = dataset.select(range(sample_size))
        text = "\n".join(dataset["text"])
    else:
        path = Path(data_path)
        if not path.exists():
            raise FileNotFoundError(f"Data file not found: {data_path}")
        text = path.read_text(encoding="utf-8")

    stoi, itos = build_vocabulary(text)
    data = encode_text(text, stoi)

    split = int(len(data) * (1.0 - val_ratio))
    train_data = data[:split]
    val_data = data[split:]

    train_loader = DataLoader(
        NextTokenDataset(train_data, block_size),
        batch_size=batch_size,
        shuffle=True,
        drop_last=True,
    )
    val_loader = DataLoader(
        NextTokenDataset(val_data, block_size),
        batch_size=batch_size,
        shuffle=False,
        drop_last=True,
    )
    return train_loader, val_loader, stoi, itos
