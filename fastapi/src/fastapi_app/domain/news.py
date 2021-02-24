from dataclasses import dataclass

from .creator import Creator


@dataclass
class News:
    content: str
    created_at: int
    creator: Creator
    id: int
    title: str
