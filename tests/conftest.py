from app.database.session import Base, engine
from app.core.config_app import config_app
from fastapi.testclient import TestClient
from typing import Generator
from fastapi import FastAPI
from unittest import mock
from typing import Any
from os import getenv
import pytest


def start_application():
    app = config_app()
    test_client = TestClient(app)
    return test_client

@pytest.fixture(scope="function")
def client() -> Generator[FastAPI, Any, None]:
    if getenv("ENVIRONMENT") == "TEST":
        import app.database.schemas
        Base.metadata.create_all(engine)

    with \
    mock.patch('logging.Logger.info'), \
    mock.patch('logging.Logger.error'):
        _app = start_application()
        yield _app

    if getenv("ENVIRONMENT") == "TEST":
        Base.metadata.drop_all(engine)
