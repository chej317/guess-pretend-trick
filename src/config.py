import torch
from dataclasses import dataclass
from typing import Optional

@dataclass
class GPTConfig:
    data_path: str = "roneneldan/TinyStories"
    is_hf: bool = True
    sample_size: Optional[int] = 5000  # Default sample size to keep it fast
    block_size: int = 128             # Increased for English stories
    batch_size: int = 64
    max_iters: int = 5000             # Increased for better learning
    eval_interval: int = 100
    eval_iters: int = 100
    learning_rate: float = 3e-4
    device: str = "cuda" if torch.cuda.is_available() else "cpu"
    n_embd: int = 192                 # Slightly larger model for English
    n_head: int = 6
    n_layer: int = 6
    dropout: float = 0.2
    val_ratio: float = 0.1
    seed: int = 42
    output_dir: str = "checkpoints"
