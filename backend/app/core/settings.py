from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    # App
    APP_NAME: str = "SupFile"
    APP_VERSION: str = "1.0.0"
    ENV: str = "dev"
    DEBUG: bool = True

    # DB : PostgreSQL
    database_url: str
    sync_database_url: str

    # DB : MinIO

    class Config:
        env_file = ".env"
        case_sensitive = False
        env_file_encoding = "utf-8"
        extra = "ignore"
        env_ignore_empty = True,

settings = Settings()
