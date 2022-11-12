from app.routes import company_routes
from fastapi import APIRouter


api_router = APIRouter()
api_router.include_router(company_routes.router, prefix="/company")
