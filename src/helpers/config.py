from pydantic import AliasChoices, Field
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=".env",
        extra="ignore",
        case_sensitive=False,
    )

    APP_NAME: str = "MINI-RAG"
    APP_VERSION: str = "0.1"
    OPENAI_API_KEY: str = None

    FILE_ALLOWED_TYPES: list = Field(default_factory=list)
    FILE_MAX_SIZE: int = 10
    FILE_DEFAULT_CHUNK_SIZE: int = 512000

    POSTGRES_USERNAME: str = None
    POSTGRES_PASSWORD: str = None
    POSTGRES_MAIN_DATABASE: str = None
    POSTGRES_HOST: str = None
    POSTGRES_PORT: int = None
     

    GENERATION_BACKEND: str = "OPENAI"
    EMBEDDING_BACKEND: str = "OPENAI"

    OPENAI_API_URL: str = None
    COHERE_API_KEY: str = None

    GENERATION_MODEL_ID: str = None
    EMBEDDING_MODEL_ID: str = None
    EMBEDDING_MODEL_SIZE: int = None
    INPUT_DAFAULT_MAX_CHARACTERS: int = None
    GENERATION_DAFAULT_MAX_TOKENS: int = None
    GENERATION_DAFAULT_TEMPERATURE: float = None

    VECTOR_DB_BACKEND: str = "QDRANT"
    VECTOR_DB_PATH: str = "qdrant_db"
    VECTOR_DB_DISTANCE_METHOD: str = "cosine"

    DEFAULT_LANG: str = "en"
    PRIMARY_LANG: str = "en"


def get_settings():
    return Settings()
