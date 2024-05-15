from app.db.base import Base
from sqlalchemy.orm import relationship, Mapped, mapped_column
from sqlalchemy import ForeignKey, String, Integer, Boolean, TIMESTAMP


class Category(Base):
    name: Mapped[str] = mapped_column(nullable=False)

    def __repr__(self):
        return f"Category {self.name}"


class Product(Base):
    name: Mapped[str] = mapped_column(nullable=False)
    price: Mapped[int] = mapped_column(nullable=False)
    quantity: Mapped[int] = mapped_column(nullable=False)
    description: Mapped[str] = mapped_column(nullable=True)
    category_id: Mapped[int] = mapped_column(ForeignKey('categorys.id'))

    def __repr__(self):
        return f"Product {self.name}"

 