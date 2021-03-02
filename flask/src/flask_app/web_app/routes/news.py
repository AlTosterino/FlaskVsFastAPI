from flask_app.shared.dto import NewsDTO
from flask_app.web_app.dependencies.database import get_database_repo
from flask_app.web_app.schemas import NewsSchemaInput

from flask import Blueprint, request

news_router = Blueprint("news", __name__)


@news_router.route("/news", methods=["POST"])
def add_news():
    db_repo = get_database_repo()
    news_schema = NewsSchemaInput(**request.get_json())
    news_dto = NewsDTO.from_news_schema(news_schema=news_schema)
    saved_news = db_repo.save_news(news=news_dto)
    return saved_news.as_dict()


@news_router.route("/news/<int:news_id>", methods=["GET"])
def get_news(news_id: int):
    db_repo = get_database_repo()
    news_from_db = db_repo.get_news(news_id=news_id)
    return news_from_db.as_dict()
