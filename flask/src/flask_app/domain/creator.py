from dataclasses import dataclass

from .base import Entity


@dataclass
class Creator(Entity):
    first_name: str
    last_name: str
