from .base import FastAPIAppError


class DatabaseRepositoryError(FastAPIAppError):
    pass


class NewsNotFoundError(DatabaseRepositoryError):
    pass
