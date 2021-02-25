from abc import ABC as Abstract
from abc import abstractmethod
from typing import Any, List

from fastapi_app.domain import News
from fastapi_app.web_app.schemas import NewsSchemaInput


class DatabaseRepository(Abstract):
    @abstractmethod
    def save_news(self, news: NewsSchemaInput) -> News:
        pass

    @abstractmethod
    def get_news(self, id: int) -> News:
        pass

    @abstractmethod
    def get_news_by_filter(self, **kwargs: Any) -> List[News]:
        pass
