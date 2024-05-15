from app import Base
from sqlalchemy.orm import Mapped, mapped_column
from enum import Enum


class Role(str, Enum):
    admin = "admin"
    user = "user"


class User(Base):

    name: Mapped[str] = mapped_column(nullable=False)
    email: Mapped[str] = mapped_column(nullable=False)
    role: Mapped[Role] = mapped_column(nullable=False, default=Role.user)
    password: Mapped[str] = mapped_column(nullable=False)

    def __repr__(self):
        return f"User {self.name}"
