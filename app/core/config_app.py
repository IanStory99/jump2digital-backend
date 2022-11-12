from app.exceptions.exception_handler import register_exception_handlers
from app.core.middleware import register_middleware
from app.core.logger import register_logger
from app.routes.base import api_router
from app.core.settings import settings
from fastapi import FastAPI


def register_routes(app: FastAPI):
    app.include_router(api_router)

def register_title(app: FastAPI):
    app.title = settings.PROJECT_NAME

def config_app():
    app = FastAPI()

    register_title(app)
    register_logger()
    register_exception_handlers(app)
    register_middleware(app)
    register_routes(app)

    return app
