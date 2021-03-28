import secrets

from pydantic import BaseSettings


class Settings(BaseSettings):
    API_V1_STR: str = "/api/v1"
    PROJECT_NAME: str = "FastAPI Trains"
    SECRET_KEY: str = secrets.token_urlsafe(32)
    SQLALCHEMY_DATABASE_URI: str = "postgresql://postgres:admin@localhost:5432/fastapi_trains"

    class Config:
        env_file = ".env"


settings = Settings()
