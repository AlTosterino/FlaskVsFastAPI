from dataclasses import dataclass

from fastapi_app.domain.base import Domain


@dataclass
class Creator(Domain):
    first_name: str
    last_name: str
