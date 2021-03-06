from fastapi_app.shared.exceptions import NewsNotFoundError
from fastapi_app.web_app.routes import news
from pydantic import ValidationError

from fastapi import FastAPI, Request, status
from fastapi.responses import JSONResponse

app = FastAPI()

app.include_router(news.router)


@app.exception_handler(NewsNotFoundError)
async def handle_news_not_found_error(request: Request, exc: NewsNotFoundError):
    return JSONResponse(
        status_code=status.HTTP_404_NOT_FOUND,
        content={"detail": str(exc)},
    )


@app.exception_handler(ValidationError)
async def handle_validation_error(request: Request, exc: ValidationError):
    return JSONResponse(
        status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
        content={"detail": exc.errors()},
    )
