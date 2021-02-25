from datetime import datetime

from pydantic import BaseModel, Field

from .creator import CreatorSchema


class NewsSchemaInput(BaseModel):
    title: str = Field(
        title="Title of the News",
        max_length=100,
        min_length=10,
        example="Clickbait title",
    )
    content: str = Field(
        title="Content of the News", min_length=50, example="Lorem ipsum..."
    )
    creator: CreatorSchema


class NewsSchemaOutput(NewsSchemaInput):
    id: int = Field(example="26")
    created_at: datetime = Field(example="1614198897")

    class Config:
        json_encoders = {datetime: lambda dt: int(dt.timestamp())}
