from dataclasses import dataclass, field

from flask_app.shared.exceptions.validation import ValidationError

from .creator import CreatorSchema, CreatorSchemaInput

MAX_TITLE_LEN = 100
MIN_TITLE_LEN = 10
MIN_CONTENT_LEN = 50


@dataclass()
class NewsSchema:
    title: str = ""
    content: str = ""
    creator: CreatorSchema = CreatorSchema()


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
            if not isinstance(self.creator, CreatorSchemaInput):
                self.creator = CreatorSchemaInput(**self.creator)  # type: ignore
        except ValidationError as err:
            self._errors["creator"] = err.errors
        if self._errors:
            raise ValidationError(
                f"Validation failed on {type(self).__name__}", self._errors
            )
