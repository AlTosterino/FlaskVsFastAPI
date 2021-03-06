from __future__ import annotations

from dataclasses import dataclass, field

from flask_app.domain import Creator
from flask_app.shared.exceptions.validation import ValidationError
from flask_app.web_app.schemas.base import BaseSchema

FIRST_NAME_MIN_LEN = 2
FIRST_NAME_MAX_LEN = 60
LAST_NAME_MIN_LEN = 2
LAST_NAME_MAX_LEN = 100


@dataclass
class CreatorSchema(BaseSchema):
    first_name: str = ""
    last_name: str = ""

    @classmethod
    def from_entity(cls, creator: Creator) -> CreatorSchema:
        return CreatorSchema(first_name=creator.first_name, last_name=creator.last_name)


@dataclass
class CreatorSchemaInput(CreatorSchema):
    _errors: dict = field(init=False, default_factory=dict)

    def _validate_first_name(self) -> None:
        if FIRST_NAME_MIN_LEN > len(self.first_name) < FIRST_NAME_MAX_LEN:
            self._errors[
                "first_name"
            ] = f"First name should be {FIRST_NAME_MIN_LEN}-{FIRST_NAME_MAX_LEN} characters long"

    def _validate_last_name(self) -> None:
        if LAST_NAME_MIN_LEN > len(self.last_name) < LAST_NAME_MAX_LEN:
            self._errors[
                "last_name"
            ] = f"Last name should be {LAST_NAME_MIN_LEN}-{LAST_NAME_MAX_LEN} characters long"

    def __post_init__(self) -> None:
        self._validate_first_name()
        self._validate_last_name()
        if self._errors:
            raise ValidationError(
                f"Validation failed on {type(self).__name__}", self._errors
            )


class CreatorSchemaOutput(CreatorSchema):
    pass
