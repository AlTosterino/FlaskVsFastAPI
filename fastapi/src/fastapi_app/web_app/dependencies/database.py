from functools import cache

from fastapi_app.infrastructure.database import DatabaseRepositoryInMemory
from fastapi_app.interfaces import DatabaseRepository


@cache  # Always return the same DB Repository
def get_database_repo() -> DatabaseRepository:
    return DatabaseRepositoryInMemory()
