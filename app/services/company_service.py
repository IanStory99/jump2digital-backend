from app.models.company_model import CompanyFiltersModel, CompanySummaryModel

from app.database.schemas.company_schema import CompanySchema
from sqlalchemy.orm import Session


class CompanyService:

    def get_all(self, db: Session, filters: CompanyFiltersModel) -> list[CompanySchema]:
        return db.query(CompanySchema).order_by(getattr(CompanySchema, filters.order)).all()

    def get_summary(self, db: Session) -> CompanySummaryModel:
        industry_count_dict = {}
        size_count_dict = {}
        founded_year_count_dict = {}

        companies: list[CompanySchema] = db.query(CompanySchema).all()

        for company in companies:
            industry_count_dict[company.industry] = industry_count_dict.get(company.industry, 0) + 1
            size_count_dict[company.size] = size_count_dict.get(company.size, 0) + 1
            founded_year_count_dict[company.founded] = founded_year_count_dict.get(company.founded, 0) + 1

        return CompanySummaryModel(
            industry_count=industry_count_dict,
            size_count=size_count_dict,
            founded_year_count=founded_year_count_dict
        )
