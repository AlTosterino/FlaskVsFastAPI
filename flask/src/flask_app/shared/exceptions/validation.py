from .base import FlaskAppError


class ValidationError(FlaskAppError):

    # TODO: Change message to be str, and errors to be dict, this will allow
    # TODO: to have message and errors together
    def __init__(self, message: dict) -> None:
        super().__init__(message)
        self.errors = dict(message)
