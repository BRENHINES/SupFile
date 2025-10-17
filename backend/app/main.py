from fastapi import FastAPI

from .api.v1.router import api_router
from .core.settings import settings

app = FastAPI(
    title=settings.APP_NAME,
    version=settings.APP_VERSION,
    summary=settings.APP_SUMMARY,
    description=settings.APP_DESCRIPTION,
    docs_url="/docs",
    redoc_url="/redoc",
)

app.include_router(api_router)
