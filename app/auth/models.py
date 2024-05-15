from app import Base
from sqlalchemy.orm import Mapped, mapped_column
from enum import Enum
from sqlalchemy import ForeignKey, String, Integer, Text


class Role(str, Enum):
    admin = "admin"
    user = "user"


class User(Base):
    username: Mapped[str] = mapped_column(
        String(32), unique=True, nullable=False)
    email: Mapped[str] = mapped_column(String(33), nullable=False, unique=True)

    def __repr__(self):
        return f"User {self.username}"


class Post(Base):
    title: Mapped[str] = mapped_column(String(100), nullable=False)
    content: Mapped[str] = mapped_column(Text, default="", server_default="")
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"))
