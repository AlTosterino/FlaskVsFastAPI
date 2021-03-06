from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime

from flask_app.domain import News
from flask_app.shared.exceptions.validation import ValidationError
from flask_app.web_app.schemas.base import BaseSchema

from .creator import CreatorSchema, CreatorSchemaInput

MAX_TITLE_LEN = 100
MIN_TITLE_LEN = 10
MIN_CONTENT_LEN = 50


@dataclass()
class NewsSchema(BaseSchema):
    title: str = ""
    content: str = ""
    creator: CreatorSchema = CreatorSchema()

    @classmethod
    def from_entity(cls, news: News) -> NewsSchema:
        return cls(
            title=news.title,
            content=news.content,
            creator=CreatorSchema.from_entity(creator=news.creator),
        )


@dataclass()
class NewsSchemaInput(NewsSchema):
    _errors: dict = field(init=False, default_factory=dict)

    def _validate_title(self) -> None:
        if MIN_TITLE_LEN > len(self.title) < MAX_TITLE_LEN:
            self._errors[
                "title"
            ] = f"Title should be {MIN_TITLE_LEN}-{MAX_TITLE_LEN} characters long"

    def _validate_content(self) -> None:
        if len(self.content) < MIN_CONTENT_LEN:
            self._errors[
                "content"
            ] = f"Content should be minimum {MIN_CONTENT_LEN} characters long"

    def __post_init__(self) -> None:
        self._validate_content()
        self._validate_title()
        try:
            if not isinstance(self.creator, CreatorSchemaInput):  # type: ignore
                self.creator = CreatorSchemaInput(**self.creator)  # type: ignore
        except ValidationError as err:
            self._errors["creator"] = err.errors
        if self._errors:
            raise ValidationError(
                f"Validation failed on {type(self).__name__}", self._errors
            )


@dataclass
class NewsSchemaOutput(NewsSchema):
    id: int = 0
    created_at: datetime = datetime.now()
    updated_at: datetime = datetime.now()

    @classmethod
    def from_entity(cls, news: News) -> NewsSchemaOutput:
        return cls(
            id=news.id,
            created_at=news.created_at,
            updated_at=news.updated_at,
            title=news.title,
            content=news.content,
            creator=CreatorSchema.from_entity(creator=news.creator),
        )

    def as_dict(self) -> dict:
        schema_as_dict = super().as_dict()
        schema_as_dict["created_at"] = int(self.created_at.timestamp())
        schema_as_dict["updated_at"] = int(self.updated_at.timestamp())
        return schema_as_dict
