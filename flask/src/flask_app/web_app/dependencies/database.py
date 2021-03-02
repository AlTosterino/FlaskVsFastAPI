from functools import cache

from flask_app.infrastructure.database import DatabaseRepositoryInMemory
from flask_app.interfaces import DatabaseRepository


@cache  # Always return the same DB Repository
def get_database_repo() -> DatabaseRepository:
    return DatabaseRepositoryInMemory()
