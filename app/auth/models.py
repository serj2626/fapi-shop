from turtle import back
from app import Base
from sqlalchemy.orm import Mapped, mapped_column, relationship
from enum import Enum
from sqlalchemy import ForeignKey, String, Integer, Text
# from typing import TYPE_CHECKING
# if TYPE_CHECKING:
#     from .users import User


class Role(str, Enum):
    admin = "admin"
    user = "user"


class User(Base):
    username: Mapped[str] = mapped_column(
        String(32), unique=True, nullable=False)
    email: Mapped[str] = mapped_column(String(33), nullable=False, unique=True)

    posts: Mapped[list["Post"]] = relationship(back_populates='user')

    def __repr__(self):
        return f"User {self.username}"


class Post(Base):
    title: Mapped[str] = mapped_column(String(100), nullable=False)
    content: Mapped[str] = mapped_column(Text, default="", server_default="")
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"))

    user: Mapped["User"] = relationship(back_populates='posts')

    def __repr__(self):
        return f"Post {self.title}"
