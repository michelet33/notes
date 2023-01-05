from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .config import Settings
from functools import lru_cache
from ..src.database.register import register_tortoise
from ..src.database.config import TORTOISE_ORM

app = FastAPI()


@lru_cache()
def get_settings():
    return Settings()


# def info(settings: Settings = Depends(get_settings)):
def info():
    settings = get_settings()
    return {
        "url_app": settings.url_app,
        "port_app": settings.port_app,
    }


setting = info()
url = f"{setting['url_app']}:{setting['port_app']}"

register_tortoise(app, config=TORTOISE_ORM, generate_schemas=False)

app.add_middleware(
    CORSMiddleware,
    allow_origins=[url],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def home():
    return "Hello, World!"



