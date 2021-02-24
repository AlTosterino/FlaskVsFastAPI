from fastapi_app.web_app.routes import news

from fastapi import FastAPI

app = FastAPI()

app.include_router(news.router)
