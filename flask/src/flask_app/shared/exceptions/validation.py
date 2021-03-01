from .base import FlaskAppError


class ValidationError(FlaskAppError):
    def __init__(self, message: str, errors: dict) -> None:
        super().__init__(message)
        self.errors = dict(errors)
