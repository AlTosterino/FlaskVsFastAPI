from __future__ import annotations

from dataclasses import asdict, dataclass


@dataclass
class BaseSchema:
    def as_dict(self) -> dict:
        schema_as_dict = asdict(self)
        schema_as_dict.pop("_errors", None)
        return schema_as_dict

    def update(self, data: dict) -> dict:
        schema_as_dict = self.as_dict()
        available_keys = schema_as_dict.keys()
        data_to_update = {}
        for key, value in data.items():
            if key in available_keys:
                data_to_update[key] = value
        schema_as_dict.update(data_to_update)
        return schema_as_dict
