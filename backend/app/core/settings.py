from pathlib import Path

from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict

BASE_DIR = Path(__file__).resolve().parent.parent.parent
ENV_FILE = BASE_DIR / ".env"


class Settings(BaseSettings):
    # App
    APP_NAME: str = "SupFile"
    APP_VERSION: str = "1.0.0"
    APP_SUMMARY : str = "A file hosting service."
    APP_DESCRIPTION : str = "SupFile is a modern file hosting service that allows users to upload, share, and manage their files with ease and security."
    ENV: str = "dev"
    DEBUG: bool = True

    # DB : PostgreSQL
    DATABASE_URL: str = Field(..., env="DATABASE_URL")
    SYNC_DATABASE_URL: str = Field(..., env="SYNC_DATABASE_URL")

    # DB : MinIO

    model_config = SettingsConfigDict(
        env_file=str(ENV_FILE),
        case_sensitive=False,
        env_file_encoding="utf-8",
        extra="ignore"
    )

settings = Settings()
