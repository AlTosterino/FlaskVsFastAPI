from flask_app.web_app.schemas import NewsSchemaInput

from flask import Blueprint, request

news_router = Blueprint("news", __name__)


@news_router.route("/news", methods=["POST"])
def add_news():
    NewsSchemaInput(**request.get_json())
    return {}
