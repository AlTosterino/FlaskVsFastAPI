from pydantic import BaseModel

from .creator import CreatorSchema


class NewsSchemaInput(BaseModel):
    title: str
    content: str
    creator: CreatorSchema


class NewsSchemaOutput(NewsSchemaInput):
    id: int
    created_at: int
