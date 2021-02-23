from dataclasses import dataclass, field
from typing import List

from pydantic import BaseModel

from fastapi import FastAPI, HTTPException

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


class DatabaseRepositoryError(Exception):
    pass


@dataclass
class NewsRepository:
    _last_id: int = field(init=False, default=0)
    _database: List[News] = field(init=False, default_factory=list)

    def save(self, news_input: NewsInput) -> News:
        self._last_id += 1
        news_to_save = News(**{"id": self._last_id, **news_input.dict()})
        self._database.append(news_to_save)
        return news_to_save

    def get(self, news_id: int) -> News:
        for news in self._database:
            if news.id == news_id:
                return news
        raise DatabaseRepositoryError(f"News with id {news_id} don't exist")


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
