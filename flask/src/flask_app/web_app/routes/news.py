from flask_app.shared.exceptions.validation import ValidationError
from flask_app.web_app.schemas import NewsSchemaInput

from flask import Blueprint, request

news_router = Blueprint("news", __name__)


@news_router.route("/news", methods=["POST"])
def add_news():
    try:
        NewsSchemaInput(**request.get_json())
    except ValidationError as err:
        return err.errors
    return {}
