from pydantic import BaseSettings
from typing import Optional
from pathlib import Path
from os import getenv


environments = {
    "LOCAL": ".env",
    "DEV": ".env.dev",
    "PROD": ".env.prod",
    "TEST": ".env.test"
}

class Settings(BaseSettings):
    PROJECT_NAME: str = "JUMP2DIGITAL-BACKEND"
    PROJECT_VERSION: str = "1.0.0"

    ENVIRONMENT: str

    DATABASE_STRING: str

    class Config:
        env_file = Path(".") / environments[getenv("ENVIRONMENT", "LOCAL")]

settings = Settings()
