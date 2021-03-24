import os
from http import HTTPStatus
from typing import Tuple

from flask_app.shared.exceptions import DatabaseRepositoryError
from flask_app.shared.exceptions.validation import ValidationError
from flask_app.web_app.routes import news_router

from flask import Flask

app = Flask(__name__)
app.register_blueprint(news_router)


@app.errorhandler(ValidationError)
def handle_validation_error(exc: ValidationError) -> Tuple[dict, int]:
    status_code = HTTPStatus.UNPROCESSABLE_ENTITY
    return {"detail": exc.errors}, status_code


@app.errorhandler(DatabaseRepositoryError)
def handle_database_error(exc: DatabaseRepositoryError) -> Tuple[dict, int]:
    status_code = HTTPStatus.BAD_REQUEST
    return {"detail": str(exc)}, status_code


if __name__ == "__main__":
    app.run(debug=True, host=os.environ.get("APP_HOST", "127.0.0.1"))
