from dataclasses import dataclass

from fastapi_app.domain.base import Entity


@dataclass
class Creator(Entity):
    first_name: str
    last_name: str
