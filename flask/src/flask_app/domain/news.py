from dataclasses import dataclass
from datetime import datetime

from .creator import Creator, Entity


@dataclass
class News(Entity):
    content: str
    created_at: datetime
    creator: Creator
    id: int
    title: str
    updated_at: datetime
