from app.models.base import BaseModel
from typing import Literal, Optional


class CompanyResponseModel(BaseModel):
    id: str
    website: Optional[str]
    name: Optional[str]
    founded: Optional[int]
    size: Optional[str]
    locality: Optional[str]
    region: Optional[str]
    country: Optional[str]
    industry: Optional[str]
    linkedin_url: Optional[str]

class CompanyFiltersModel(BaseModel):
    order: Literal["founded"] | Literal["size"]

class CompanySummaryModel(BaseModel):
    industry_count: dict
    size_count: dict
    founded_year_count: dict
