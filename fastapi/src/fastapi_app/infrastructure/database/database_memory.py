from dataclasses import dataclass, field
from datetime import datetime
from typing import Any, List

from fastapi_app.domain import Creator, News
from fastapi_app.interfaces import DatabaseRepository
from fastapi_app.shared.exceptions import DatabaseRepositoryError
from fastapi_app.web_app.schemas import NewsSchemaInput


@dataclass
class DatabaseRepositoryInMemory(DatabaseRepository):
    _last_id: int = field(init=False, default=0)
    _database: List[News] = field(init=False, default_factory=list)

    def save(self, news_input: NewsSchemaInput) -> News:
        self._last_id += 1
        created_at = int(datetime.now().timestamp())
        news_to_save = News(
            id=self._last_id,
            created_at=created_at,
            creator=Creator(
                first_name=news_input.creator.first_name,
                last_name=news_input.creator.last_name,
            ),
            title=news_input.title,
            content=news_input.content,
        )
        self._database.append(news_to_save)
        return news_to_save

    def get(self, news_id: int) -> News:
        for news in self._database:
            if news.id == news_id:
                return news
        raise DatabaseRepositoryError(f"News with id {news_id} don't exist")

    def get_by_filter(self, distinct: bool = True, **kwargs: Any) -> List[News]:
        news_result = list()
        for news in self._database:
            for attr_name, attr_value in kwargs.items():
                if getattr(news, attr_name, None) in attr_value:
                    news_result.append(news)
        if distinct:
            # dict.fromkeys -> Make sure to have ordered set
            news_result = list(dict.fromkeys(news_result))
        return list(news_result)
