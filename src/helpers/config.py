from functools import lru_cache

from pydantic import AliasChoices, Field
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):

    APP_NAME: str
    APP_VERSION: str
    OPENAI_API_KEY: str

    FILE_ALLOWED_TYPES: list
    FILE_MAX_SIZE: int
    FILE_DEFAULT_CHUNK_SIZE: int

    MONGODB_URL: str = Field(
        validation_alias=AliasChoices("MONGODB_URL", "MONGO_DB_URL")
    )
    MONGODB_DATABASE: str = Field(
        validation_alias=AliasChoices("MONGODB_DATABASE", "MONGO_DB_NAME")
    )

    model_config = SettingsConfigDict(
        env_file=".env",
        extra="ignore",
    )


@lru_cache
def get_settings():
    return Settings()
