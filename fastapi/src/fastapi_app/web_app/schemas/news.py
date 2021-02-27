from __future__ import annotations

from datetime import datetime
from typing import Any

from pydantic import BaseModel, Field

from .creator import CreatorSchema, CreatorSchemaInput, CreatorSchemaUpdate


class NewsSchema(BaseModel):
    title: str = ""
    content: str = ""
    creator: CreatorSchema


class NewsSchemaInput(NewsSchema):
    title: str = Field(
        title="Title of the News",
        max_length=100,
        min_length=10,
        example="Clickbait title",
    )
    content: str = Field(
        title="Content of the News", min_length=50, example="Lorem ipsum..."
    )
    creator: CreatorSchemaInput

    def copy(self, *args: Any, **kwargs: Any) -> NewsSchema:  # type: ignore
        if creator := kwargs.get("update", {}).get("creator"):
            updated_creator = self.creator.copy(update=creator)
            kwargs["update"]["creator"] = updated_creator
        updated_schema = super().copy(*args, **kwargs)
        return updated_schema


class NewsSchemaOutput(NewsSchema):
    id: int = Field(example="26")
    created_at: datetime = Field(example="1614198897")
    updated_at: datetime = Field(example="1614198897")

    class Config:
        json_encoders = {datetime: lambda dt: int(dt.timestamp())}


class NewsSchemaUpdate(NewsSchema):
    title: str = ""
    content: str = ""
    creator: CreatorSchemaUpdate = CreatorSchemaUpdate()
