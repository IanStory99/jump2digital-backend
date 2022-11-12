from sqlalchemy import Column, Integer, String
from app.database.session import Base


class CompanySchema(Base):
    __tablename__ = 'company'

    id = Column(String(100), primary_key=True, unique=True)
    website = Column(String(100))
    name = Column(String(100))
    founded = Column(Integer)
    size = Column(String(50))
    locality = Column(String(100))
    region = Column(String(100))
    country = Column(String(100))
    industry = Column(String(200))
    linkedin_url = Column(String(300))

    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)

    def __repr__(self):
        return f"<Company {self.name}>"
