from abc import ABC as Abstract
from abc import abstractmethod
from typing import Any, List

from flask_app.domain import News
from flask_app.shared.dto import NewsDTO


class DatabaseRepository(Abstract):
    @abstractmethod
    def save_news(self, news_dto: NewsDTO) -> News:
        pass

    @abstractmethod
    def delete_news(self, news_id: int) -> None:
        pass

    @abstractmethod
    def update_news(self, news_id: int, news_dto: NewsDTO) -> News:
        pass

    @abstractmethod
    def get_news(self, news_id: int) -> News:
        pass

    @abstractmethod
    def get_news_by_filter(self, **kwargs: Any) -> List[News]:
        pass
