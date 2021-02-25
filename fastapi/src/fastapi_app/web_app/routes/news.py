from datetime import datetime
from typing import List, Set

from fastapi_app.infrastructure.database import DatabaseRepositoryInMemory
from fastapi_app.shared.exceptions import DatabaseRepositoryError
from fastapi_app.web_app.schemas import NewsSchemaInput, NewsSchemaOutput

from fastapi import APIRouter, HTTPException, Query

router = APIRouter()

DATABASE_REPOSITORY = DatabaseRepositoryInMemory()


@router.post("/news", response_model=NewsSchemaOutput, summary="Create the news")
def add_news(news_input: NewsSchemaInput):
    """
    Create the news with following information:

    - **title**: Title of news
    - **content**: News content
    - **creator**: Creator of content
    """
    db_news = DATABASE_REPOSITORY.save_news(news_input=news_input)
    return db_news.as_dict()


@router.get(
    "/news/{news_id}",
    response_model=NewsSchemaOutput,
    summary="Get the news by ID",
    responses={
        404: {
            "description": "News with given ID wasn't found",
            "content": {
                "application/json": {
                    "example": {"detail": "News with id {id} don't exist"}
                }
            },
        }
    },
)
def get_news(news_id: int):
    """
    Get the news with passed ID
    """
    try:
        db_news = DATABASE_REPOSITORY.get_news(news_id=news_id)
    except DatabaseRepositoryError as err:
        raise HTTPException(status_code=404, detail=str(err))
    return db_news.as_dict()


@router.get(
    "/news",
    response_model=List[NewsSchemaOutput],
    summary="Get the news by filter",
)
def get_news_by_filter(
    id: Set[int] = Query(set()), created_at: Set[datetime] = Query(set())
):
    """
    Get the news with passed filters.

    - **id**: List of id to search for
    - **created_at**: List of date of creation timestamps
    """
    try:
        db_news = DATABASE_REPOSITORY.get_news_by_filter(id=id, created_at=created_at)
    except DatabaseRepositoryError as err:
        raise HTTPException(status_code=404, detail=str(err))
    return [news.as_dict() for news in db_news]
