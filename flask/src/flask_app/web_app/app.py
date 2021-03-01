from http import HTTPStatus
from typing import Tuple

from flask_app.shared.exceptions.validation import ValidationError
from flask_app.web_app.routes import news_router

from flask import Flask

app = Flask(__name__)
app.register_blueprint(news_router)


@app.errorhandler(ValidationError)
def handle_validation_error(exc: ValidationError) -> Tuple[dict, int]:
    status_code = HTTPStatus.UNPROCESSABLE_ENTITY
    return {"details": exc.errors}, status_code


if __name__ == "__main__":
    app.run(debug=True)
