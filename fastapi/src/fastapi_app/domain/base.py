from abc import ABC as Abstract
from dataclasses import asdict


class Domain(Abstract):
    def as_dict(self) -> dict:
        return asdict(self)
