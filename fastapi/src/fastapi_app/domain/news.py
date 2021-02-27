from dataclasses import dataclass
from datetime import datetime

from fastapi_app.domain.base import Entity

from .creator import Creator


@dataclass
class News(Entity):
    content: str
    created_at: datetime
    creator: Creator
    id: int
    title: str
    updated_at: datetime
