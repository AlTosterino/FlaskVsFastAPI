from abc import ABC as Abstract
from dataclasses import asdict


class Entity(Abstract):
    def as_dict(self) -> dict:
        return asdict(self)
