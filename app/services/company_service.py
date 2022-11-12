from app.models.company_model import CompanyFiltersModel, CompanySummaryModel
from app.database.schemas.company_schema import CompanySchema
from sqlalchemy.orm import Session
from re import sub


class CompanyService:

    def get_all(self, db: Session, filters: CompanyFiltersModel) -> list[CompanySchema]:
        companies = db.query(CompanySchema).order_by(getattr(CompanySchema, filters.order)).all()

        if filters.order == "size":
            companies = self._handle_size_order(companies)

        return companies

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

    def _handle_size_order(self, companies: list[CompanySchema]) -> list[CompanySchema]:
        return sorted(companies, key=lambda company: self._size_string_range_to_int_average(company.size))

    def _size_string_range_to_int_average(self, size_range: str) -> int:
        if "-" not in size_range:
            size_range = sub(r"\D", "", size_range)
            return int(size_range)

        return sum([int(size) for size in size_range.split("-")]) / 2
