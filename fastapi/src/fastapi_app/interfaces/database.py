from abc import ABC as Abstract
from abc import abstractmethod
from typing import Any, List

from fastapi_app.domain import News
from fastapi_app.web_app.schemas import NewsSchemaInput


class DatabaseRepository(Abstract):
    @abstractmethod
    def save(self, news: NewsSchemaInput) -> News:
        pass

    @abstractmethod
    def get(self, id: int) -> News:
        pass

    @abstractmethod
    def get_by_filter(self, distinct: bool = True, **kwargs: Any) -> List[News]:
        pass
