from dataclasses import asdict, dataclass
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

    def as_dict(self) -> dict:
        news_as_dict = asdict(self)
        news_as_dict["created_at"] = int(self.created_at.timestamp())
        news_as_dict["updated_at"] = int(self.created_at.timestamp())
        return news_as_dict
