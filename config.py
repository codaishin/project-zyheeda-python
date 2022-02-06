from dataclasses import dataclass
from typing import Tuple


@dataclass
class Settings:
    """game settings"""

    size: Tuple[int, int]
    fps: int


SETTINGS = Settings(
    size=(800, 600),
    fps=30,
)
