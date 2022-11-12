from fastapi.responses import JSONResponse
from app.exceptions.exceptions import *
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

    @app.exception_handler(BadRequestException)
    async def exception_handler(request: Request, exc: BadRequestException):
        return handle_exception_response(request, exc.content, exc.status, exc.message)

    @app.exception_handler(UnauthorizedException)
    async def exception_handler(request: Request, exc: UnauthorizedException):
        return handle_exception_response(request, exc.content, exc.status, exc.message)

    @app.exception_handler(ForbiddenException)
    async def exception_handler(request: Request, exc: ForbiddenException):
        return handle_exception_response(request, exc.content, exc.status, exc.message)

    @app.exception_handler(NotFoundException)
    async def exception_handler(request: Request, exc: NotFoundException):
        return handle_exception_response(request, exc.content, exc.status, exc.message)

    @app.exception_handler(NotAcceptableException)
    async def exception_handler(request: Request, exc: NotAcceptableException):
        return handle_exception_response(request, exc.content, exc.status, exc.message)

    @app.exception_handler(RequestTimeoutException)
    async def exception_handler(request: Request, exc: RequestTimeoutException):
        return handle_exception_response(request, exc.content, exc.status, exc.message)

    @app.exception_handler(ConflictException)
    async def exception_handler(request: Request, exc: ConflictException):
        return handle_exception_response(request, exc.content, exc.status, exc.message)

    @app.exception_handler(GoneException)
    async def exception_handler(request: Request, exc: GoneException):
        return handle_exception_response(request, exc.content, exc.status, exc.message)

    @app.exception_handler(UnprocessableException)
    async def exception_handler(request: Request, exc: UnprocessableException):
        return handle_exception_response(request, exc.content, exc.status, exc.message)

    @app.exception_handler(LockedException)
    async def exception_handler(request: Request, exc: LockedException):
        return handle_exception_response(request, exc.content, exc.status, exc.message)

    @app.exception_handler(FailedDependencyException)
    async def exception_handler(request: Request, exc: FailedDependencyException):
        return handle_exception_response(request, exc.content, exc.status, exc.message)

    @app.exception_handler(TooManyRequestsException)
    async def exception_handler(request: Request, exc: TooManyRequestsException):
        return handle_exception_response(request, exc.content, exc.status, exc.message)

    @app.exception_handler(NotImplementedException)
    async def exception_handler(request: Request, exc: NotImplementedException):
        return handle_exception_response(request, exc.content, exc.status, exc.message)

    @app.exception_handler(ServiceUnavailableException)
    async def exception_handler(request: Request, exc: ServiceUnavailableException):
        return handle_exception_response(request, exc.content, exc.status, exc.message)

    @app.exception_handler(InsufficientStorageException)
    async def exception_handler(request: Request, exc: InsufficientStorageException):
        return handle_exception_response(request, exc.content, exc.status, exc.message)

    @app.exception_handler(Exception)
    async def exception_handler(request: Request, exc: Exception):
        return handle_exception_response(request, exc, 500, "Internal server error")
