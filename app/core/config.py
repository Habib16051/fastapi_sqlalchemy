from pydantic_settings import BaseSettings
import os
class Settings(BaseSettings):
    PROJECT_NAME: str = "E-commerce API"
    API_V1_STR: str = "/api/v1"

    PROJECT_SERVER: str = "http://localhost:8000"
    PROJECT_VERSION: str = "1.0.0"
    PROJECT_DESCRIPTION: str = "An e-commerce API for managing products, orders, and users."

    # DB settings
    DATABASE_URL: str = os.getenv("DATABASE_URL")


    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"

settings = Settings()
