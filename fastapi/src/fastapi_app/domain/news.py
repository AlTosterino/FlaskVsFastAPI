from dataclasses import dataclass
from datetime import datetime

from fastapi_app.domain.base import Domain

from .creator import Creator


@dataclass
class News(Domain):
    content: str
    created_at: datetime
    creator: Creator
    id: int
    title: str
    updated_at: datetime
