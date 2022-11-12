from app.models.company_model import CompanyResponseModel, CompanySummaryModel, CompanyFiltersModel
from app.services.company_service import CompanyService
from app.models.response import Response
from app.database.session import get_db
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session


router = APIRouter()

@router.get("/", response_model=Response[list[CompanyResponseModel]])
async def get_all(
    filters: CompanyFiltersModel = Depends(),
    company_service: CompanyService = Depends(CompanyService),
    db: Session = Depends(get_db)
):
    companies = company_service.get_all(db, filters)
    return Response(success=True, message="Compañías obtenidas correctamente", item=companies)

@router.get("/summary", response_model=Response[CompanySummaryModel])
async def get_summary(
    company_service: CompanyService = Depends(CompanyService),
    db: Session = Depends(get_db)
):
    summary = company_service.get_summary(db)
    return Response(success=True, message="Resumen obtenido correctamente", item=summary)
