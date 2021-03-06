from datetime import datetime
from typing import List, Set

from fastapi_app.interfaces import DatabaseRepository
from fastapi_app.shared.dto import NewsDTO
from fastapi_app.web_app.dependencies.database import get_database_repo
from fastapi_app.web_app.responses import NOT_FOUND_FOR_ID
from fastapi_app.web_app.schemas import NewsSchemaInput, NewsSchemaOutput
from fastapi_app.web_app.schemas.news import NewsSchema, NewsSchemaUpdate

from fastapi import APIRouter, Depends, Query, Response, status

router = APIRouter()


@router.post(
    "/news",
    response_model=NewsSchemaOutput,
    summary="Create the news",
    status_code=status.HTTP_201_CREATED,
)
async def add_news(
    news_input: NewsSchemaInput,
    db_repo: DatabaseRepository = Depends(get_database_repo),
):
    """
    Create the news with following information:

    - **title**: Title of news
    - **content**: News content
    - **creator**: Creator of content
    """
    news_dto = NewsDTO.from_news_schema(news_schema=news_input)
    db_news = await db_repo.save_news(news_dto=news_dto)
    return db_news.as_dict()


@router.delete(
    "/news/{news_id}",
    summary="Delete the news",
    status_code=status.HTTP_204_NO_CONTENT,
    responses=NOT_FOUND_FOR_ID,
)
async def delete_news(
    news_id: int,
    db_repo: DatabaseRepository = Depends(get_database_repo),
):
    """
    Delete News with given id
    """
    await db_repo.delete_news(news_id=news_id)
    return Response(status_code=status.HTTP_204_NO_CONTENT)


@router.put(
    "/news/{news_id}",
    summary="Overwrite the news",
    status_code=status.HTTP_204_NO_CONTENT,
    responses=NOT_FOUND_FOR_ID,
)
async def overwrite_news(
    news_id: int,
    news_input: NewsSchemaInput,
    db_repo: DatabaseRepository = Depends(get_database_repo),
):
    """
    Overwrite news with passed information
    """
    news_dto = NewsDTO.from_news_schema(news_schema=news_input)
    await db_repo.update_news(news_id=news_id, news_dto=news_dto)
    return Response(status_code=status.HTTP_204_NO_CONTENT)


@router.patch(
    "/news/{news_id}",
    summary="Update the news",
    status_code=status.HTTP_204_NO_CONTENT,
    responses=NOT_FOUND_FOR_ID,
)
async def update_news(
    news_id: int,
    news_input: NewsSchemaUpdate,
    db_repo: DatabaseRepository = Depends(get_database_repo),
):
    """
    Update news with passed information
    """
    news_from_db = await db_repo.get_news(news_id=news_id)
    news_from_db_as_schema = NewsSchema(**news_from_db.as_dict())
    data_to_update = news_input.dict(exclude_unset=True)
    updated_news_schema = news_from_db_as_schema.copy(update=data_to_update)
    news_input_schema: NewsSchemaInput = NewsSchemaInput(
        **updated_news_schema.dict()
    )  # Validate
    news_dto = NewsDTO.from_news_schema(news_schema=news_input_schema)
    await db_repo.update_news(news_id=news_id, news_dto=news_dto)
    return Response(status_code=status.HTTP_204_NO_CONTENT)


@router.get(
    "/news/{news_id}",
    response_model=NewsSchemaOutput,
    summary="Get the news by ID",
    responses=NOT_FOUND_FOR_ID,
)
async def get_news(
    news_id: int, db_repo: DatabaseRepository = Depends(get_database_repo)
):
    """
    Get the news with passed ID
    """
    db_news = await db_repo.get_news(news_id=news_id)
    return db_news.as_dict()


@router.get(
    "/news",
    response_model=List[NewsSchemaOutput],
    summary="Get the news by filter",
    responses=NOT_FOUND_FOR_ID,
)
async def get_news_by_filter(
    id: Set[int] = Query(set()),
    created_at: Set[datetime] = Query(set()),
    db_repo: DatabaseRepository = Depends(get_database_repo),
):
    """
    Get the news with passed filters.

    - **id**: List of id to search for
    - **created_at**: List of date of creation timestamps
    """
    db_news = await db_repo.get_news_by_filter(id=id, created_at=created_at)
    return [news.as_dict() for news in db_news]
