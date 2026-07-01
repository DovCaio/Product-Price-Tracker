from datetime import datetime

from sqlalchemy import (
    Column,
    Integer,
    String,
    Float,
    DateTime,
    ForeignKey
)

from sqlalchemy.orm import (
    declarative_base,
    relationship
)


Base = declarative_base()


class Product(Base):

    __tablename__ = "products"


    id = Column(
        Integer,
        primary_key=True
    )


    name = Column(
        String,
        nullable=False
    )


    url = Column(
        String,
        unique=True,
        nullable=False
    )


    store = Column(
        String,
        nullable=False
    )


    created_at = Column(
        DateTime,
        default=datetime.now
    )


    prices = relationship(
        "PriceHistory",
        back_populates="product"
    )



class PriceHistory(Base):

    __tablename__ = "price_history"


    id = Column(
        Integer,
        primary_key=True
    )


    product_id = Column(
        Integer,
        ForeignKey(
            "products.id"
        ),
        nullable=False
    )


    price = Column(
        Float,
        nullable=False
    )


    checked_at = Column(
        DateTime,
        default=datetime.now
    )


    product = relationship(
        "Product",
        back_populates="prices"
    )