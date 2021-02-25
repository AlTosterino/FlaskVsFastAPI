from dataclasses import dataclass

from fastapi_app.domain.base import Domain

from .creator import Creator


@dataclass
class News(Domain):
    content: str
    created_at: int
    creator: Creator
    id: int
    title: str
