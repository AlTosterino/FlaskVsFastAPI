from __future__ import annotations

from dataclasses import dataclass

from fastapi_app.shared.dto.creator import CreatorDTO
from fastapi_app.web_app.schemas import NewsSchemaInput


@dataclass
class NewsDTO:
    title: str
    content: str
    creator: CreatorDTO

    @classmethod
    def from_news_schema(cls, news_schema: NewsSchemaInput) -> NewsDTO:
        return NewsDTO(
            title=news_schema.title,
            content=news_schema.content,
            creator=CreatorDTO(
                first_name=news_schema.creator.first_name,
                last_name=news_schema.creator.last_name,
            ),
        )
