from __future__ import annotations

from dataclasses import asdict, dataclass


@dataclass
class BaseSchema:
    def as_dict(self) -> dict:
        schema_as_dict = asdict(self)
        schema_as_dict.pop("_errors")
        return schema_as_dict
