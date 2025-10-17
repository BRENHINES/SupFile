from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    # App
    APP_NAME: str = "SupFile"
    APP_VERSION: str = "1.0.0"
    APP_SUMMARY : str = "A file hosting service."
    APP_DESCRIPTION : str = "SupFile is a modern file hosting service that allows users to upload, share, and manage their files with ease and security."
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
