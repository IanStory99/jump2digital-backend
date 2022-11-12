from app.database.schemas.company_schema import CompanySchema
from app.database.session import SessionDB


def before_insert_company(**kwargs):
    db = SessionDB()
    db.add(CompanySchema(
        id=kwargs.get('id', 'id1'),
        website=kwargs.get('website', 'website1'),
        name=kwargs.get('name', 'name1'),
        founded=kwargs.get('founded', 2000),
        size=kwargs.get('size', '1-10'),
        locality=kwargs.get('locality', 'locality1'),
        region=kwargs.get('region', 'region1'),
        country=kwargs.get('country', 'country1'),
        industry=kwargs.get('industry', 'industry1'),
        linkedin_url=kwargs.get('linkedin_url', 'linkedin_url1')
    ))
    db.commit()
