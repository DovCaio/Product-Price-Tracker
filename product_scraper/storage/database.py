from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from .models import Base

DATABASE_URL = (
    "postgresql://scraper:password@localhost:5432/products"
)


engine = create_engine(
    DATABASE_URL
)


Session = sessionmaker(
    bind=engine
)


def init_database():

    Base.metadata.create_all(
        engine
    )