import torch
from dataclasses import dataclass

@dataclass
class GPTConfig:
    data_path: str = "data/input.txt"
    block_size: int = 64
    batch_size: int = 64
    max_iters: int = 2000
    eval_interval: int = 500
    eval_iters: int = 200
    learning_rate: float = 3e-4
    device: str = "cuda" if torch.cuda.is_available() else "cpu"
    n_embd: int = 128
    n_head: int = 4
    n_layer: int = 4
    dropout: float = 0.1
    val_ratio: float = 0.1
    seed: int = 42
    output_dir: str = "checkpoints"
