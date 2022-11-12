from fastapi.responses import JSONResponse
from fastapi import FastAPI, Request
import logging


def register_exception_handlers(app: FastAPI):
    def log_exception(request: Request, request_uuid: str, exc_content, exc_status: int):
        logger = logging.getLogger("root")
        logger.error(f"EXCEPTION {request_uuid} {request.url.path} {request.method} {exc_status} {str(exc_content)}")

    def handle_exception_response(request: Request, exc_content, exc_status: int, exc_message: str):
        request_uuid = request.state.__getattr__("request_uuid")
        log_exception(request, request_uuid, exc_content, exc_status)

        response_content = {
            'code': request_uuid,
            'success': False,
            'message': exc_message
        }

        return JSONResponse(status_code=exc_status, content=response_content)

    @app.exception_handler(Exception)
    async def exception_handler(request: Request, exc: Exception):
        return handle_exception_response(request, exc, 500, "Internal server error")
