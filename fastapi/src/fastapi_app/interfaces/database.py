from abc import ABC as Abstract
from abc import abstractmethod
from typing import Any, List

from fastapi_app.domain import News
from fastapi_app.web_app.schemas import NewsSchemaInput


class DatabaseRepository(Abstract):
    @abstractmethod
    async def save_news(self, news_input: NewsSchemaInput) -> News:
        pass

    @abstractmethod
    async def delete_news(self, news_id: int) -> None:
        pass

    @abstractmethod
    async def update_news(self, news_id: int, news_input: NewsSchemaInput) -> News:
        pass

    @abstractmethod
    async def get_news(self, news_id: int) -> News:
        pass

    @abstractmethod
    async def get_news_by_filter(self, **kwargs: Any) -> List[News]:
        pass
