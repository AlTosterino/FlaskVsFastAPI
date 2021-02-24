from typing import List, Set

from fastapi_app.infrastructure.database import DatabaseRepositoryInMemory
from fastapi_app.shared.exceptions import DatabaseRepositoryError
from fastapi_app.web_app.schemas import NewsSchemaInput, NewsSchemaOutput

from fastapi import FastAPI, HTTPException, Query

app = FastAPI()

DATABASE_REPOSITORY = DatabaseRepositoryInMemory()


@app.post("/news", response_model=NewsSchemaOutput)
def add_news(news_input: NewsSchemaInput):
    return DATABASE_REPOSITORY.save(news_input=news_input)


@app.get("/news/{news_id}", response_model=NewsSchemaOutput)
def get_news(news_id: int):
    try:
        db_news = DATABASE_REPOSITORY.get(news_id=news_id)
    except DatabaseRepositoryError as err:
        raise HTTPException(status_code=404, detail=str(err))
    return db_news


@app.get("/news", response_model=List[NewsSchemaOutput])
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
