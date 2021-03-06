from flask_app.shared.dto import NewsDTO
from flask_app.web_app.dependencies.database import get_database_repo
from flask_app.web_app.schemas import NewsSchemaInput
from flask_app.web_app.schemas.news import NewsSchema, NewsSchemaOutput

from flask import Blueprint, jsonify, request

news_router = Blueprint("news", __name__)


@news_router.route("/news", methods=["POST"])
def add_news():
    db_repo = get_database_repo()
    news_schema = NewsSchemaInput(**request.get_json())
    news_dto = NewsDTO.from_news_schema(news_schema=news_schema)
    saved_news = db_repo.save_news(news_dto=news_dto)
    output_schema = NewsSchemaOutput.from_entity(news=saved_news).as_dict()
    return output_schema


@news_router.route("/news/<int:news_id>", methods=["GET"])
def get_news(news_id: int):
    db_repo = get_database_repo()
    news_from_db = db_repo.get_news(news_id=news_id)
    output_schema = NewsSchemaOutput.from_entity(news=news_from_db).as_dict()
    return output_schema


@news_router.route("/news/<int:news_id>", methods=["PUT"])
def update_news(news_id: int):
    db_repo = get_database_repo()
    news_from_db = db_repo.get_news(news_id=news_id)
    news_as_schema = NewsSchema.from_entity(news=news_from_db)
    updated_schema = news_as_schema.update(request.get_json())
    input_schema = NewsSchemaInput(**updated_schema)
    dto = NewsDTO.from_news_schema(news_schema=input_schema)
    db_repo.update_news(news_id=news_id, news_dto=dto)
    return b""


@news_router.route("/news", methods=["GET"])
def get_news_by_filter():
    db_repo = get_database_repo()
    ids = request.args.getlist("id", type=int)
    created_at = request.args.getlist("created_at", type=int)
    news_from_db = db_repo.get_news_by_filter(id=ids, created_at=created_at)
    return jsonify(
        [NewsSchemaOutput.from_entity(news=news).as_dict() for news in news_from_db]
    )
