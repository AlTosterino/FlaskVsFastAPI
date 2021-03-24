from dataclasses import dataclass, field
from datetime import datetime, timezone
from typing import Any, Dict, List

from flask_app.domain import Creator, News
from flask_app.interfaces import DatabaseRepository
from flask_app.shared.dto import NewsDTO
from flask_app.shared.exceptions import DatabaseRepositoryError


@dataclass
class DatabaseRepositoryInMemory(DatabaseRepository):
    _last_id: int = field(init=False, default=0)
    _database: Dict[int, News] = field(init=False, default_factory=dict)

    def save_news(self, news_dto: NewsDTO) -> News:
        self._last_id += 1
        now = datetime.now(tz=timezone.utc).replace(microsecond=0)
        news_to_save = News(
            id=self._last_id,
            created_at=now,
            updated_at=now,
            creator=Creator(
                first_name=news_dto.creator.first_name,
                last_name=news_dto.creator.last_name,
            ),
            title=news_dto.title,
            content=news_dto.content,
        )
        self._database[self._last_id] = news_to_save
        return news_to_save

    def delete_news(self, news_id: int) -> None:
        try:
            self._database.pop(news_id)
        except KeyError:
            raise DatabaseRepositoryError(f"News with id {news_id} don't exist")
        return

    def update_news(self, news_id: int, news_dto: NewsDTO) -> News:
        news_from_db = self.get_news(news_id=news_id)
        now = datetime.now(tz=timezone.utc).replace(microsecond=0)
        news_to_update = News(
            id=news_from_db.id,
            created_at=news_from_db.created_at,
            updated_at=now,
            creator=Creator(
                first_name=news_dto.creator.first_name,
                last_name=news_dto.creator.last_name,
            ),
            title=news_dto.title,
            content=news_dto.content,
        )
        self._database[news_to_update.id] = news_to_update
        return news_to_update

    def get_news(self, news_id: int) -> News:
        try:
            return self._database[news_id]
        except KeyError:
            raise DatabaseRepositoryError(f"News with id {news_id} don't exist")

    def get_news_by_filter(self, **kwargs: Any) -> List[News]:
        news_result = list()
        for news in self._database.values():
            for attr_name, attr_value in kwargs.items():
                if getattr(news, attr_name, None) in attr_value:
                    if news not in news_result:
                        news_result.append(news)
        return news_result
