from fastapi import FastAPI, Request, Response
import logging
import uuid


def register_middleware(app: FastAPI):
    @app.middleware("http")
    async def logging_middleware(request: Request, call_next):
        logger = logging.getLogger("root")
        request_uuid = str(uuid.uuid4())
        request.state.__setattr__("request_uuid", request_uuid)

        logger.info(f"REQUEST {request_uuid} {request.url.path} {request.method}")

        response: Response = await call_next(request)

        logger.info(f"RESPONSE {request_uuid} {request.url.path} {request.method} {response.status_code}")

        return response
