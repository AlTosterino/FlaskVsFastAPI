from dataclasses import dataclass, field
from datetime import datetime
from typing import Any, List, Set

from pydantic import BaseModel

from fastapi import FastAPI, HTTPException, Query

app = FastAPI()


class Creator(BaseModel):
    first_name: str
    last_name: str


class NewsInput(BaseModel):
    title: str
    content: str
    creator: Creator


class News(NewsInput):
    id: int
    created_at: int

    def __hash__(self):
        # Adding this object to dict required __hash__ to be implemented
        return hash(self.id + self.created_at)


class DatabaseRepositoryError(Exception):
    pass


@dataclass
class NewsRepository:
    _last_id: int = field(init=False, default=0)
    _database: List[News] = field(init=False, default_factory=list)

    def save(self, news_input: NewsInput) -> News:
        self._last_id += 1
        created_at = int(datetime.now().timestamp())
        news_to_save = News(
            **{"id": self._last_id, "created_at": created_at, **news_input.dict()}
        )
        self._database.append(news_to_save)
        return news_to_save

    def get(self, news_id: int) -> News:
        for news in self._database:
            if news.id == news_id:
                return news
        raise DatabaseRepositoryError(f"News with id {news_id} don't exist")

    def get_by_filter(self, distinct: bool, **kwargs: Any) -> List[News]:
        news_result = list()
        for news in self._database:
            for attr_name, attr_value in kwargs.items():
                if getattr(news, attr_name, None) in attr_value:
                    news_result.append(news)
        if distinct:
            # dict.fromkeys -> Make sure to have ordered set
            news_result = list(dict.fromkeys(news_result))
        return list(news_result)


DATABASE_REPOSITORY = NewsRepository()


@app.post("/news", response_model=News)
def add_news(news_input: NewsInput):
    return DATABASE_REPOSITORY.save(news_input=news_input)


@app.get("/news/{news_id}", response_model=News)
def get_news(news_id: int):
    try:
        db_news = DATABASE_REPOSITORY.get(news_id=news_id)
    except DatabaseRepositoryError as err:
        raise HTTPException(status_code=404, detail=str(err))
    return db_news


@app.get("/news", response_model=List[News])
def get_news_by_filter(
    id: Set[int] = Query(set()),
    created_at: Set[int] = Query(set()),
    distinct: bool = True,
):
    try:
        db_news = DATABASE_REPOSITORY.get_by_filter(
            distinct=distinct, id=id, created_at=created_at
        )
    except DatabaseRepositoryError as err:
        raise HTTPException(status_code=404, detail=str(err))
    return db_news
