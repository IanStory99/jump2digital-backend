from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine, event
from sqlalchemy.orm import sessionmaker
from app.core.settings import settings
from sqlalchemy.pool import StaticPool
from sqlalchemy.engine import Engine


SQLALCHEMY_DATABASE_URL = settings.DATABASE_STRING

# Testing parameters
poolclass = StaticPool if settings.ENVIRONMENT == "TEST" else None
connect_args = {"check_same_thread": False} if settings.ENVIRONMENT == "TEST" else {}

engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args=connect_args, poolclass=poolclass)
SessionDB = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

def get_db():
    try:
        db = SessionDB()
        yield db
    finally:
        db.close()

@event.listens_for(Engine, "connect")
def set_sqlite_pragma(dbapi_connection, connection_record):
    if SQLALCHEMY_DATABASE_URL and SQLALCHEMY_DATABASE_URL.startswith('sqlite://'):
        cursor = dbapi_connection.cursor()
        cursor.execute("PRAGMA foreign_keys=ON")
        cursor.close()
