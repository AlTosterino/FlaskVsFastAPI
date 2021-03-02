from dataclasses import asdict, dataclass

from .base import Entity


@dataclass
class Creator(Entity):
    first_name: str
    last_name: str

    def as_dict(self) -> dict:
        return asdict(self)
