from turtle import back
from app import Base
from sqlalchemy.orm import Mapped, mapped_column, relationship
from enum import Enum
from sqlalchemy import ForeignKey, String, Integer, Text
from .mixins import UserRelationMixin


# from typing import TYPE_CHECKING
# if TYPE_CHECKING:
#     from .users import User


class Role(str, Enum):
    admin = "admin"
    user = "user"


class User(Base):

    username: Mapped[str] = mapped_column(String(32), unique=True, nullable=False)
    email: Mapped[str] = mapped_column(String(33), nullable=False, unique=True)
    posts: Mapped[list["Post"]] = relationship(back_populates="user")
    profile: Mapped["Profile"] = relationship(back_populates="user")

    def __repr__(self):
        return f"User {self.username}"


class Post(UserRelationMixin, Base):
    _user_back_populates = "posts"

    title: Mapped[str] = mapped_column(String(100), nullable=False)
    body: Mapped[str] = mapped_column(Text, default="", server_default="")

    def __repr__(self):
        return f"Post {self.title}"


class Profile(UserRelationMixin, Base):
    _user_id_unique = True
    _user_back_populates = "profile"

    first_name: Mapped[str | None] = mapped_column(String(30))
    last_name: Mapped[str | None] = mapped_column(String(30))
    bio: Mapped[str | None]

    def __repr__(self):
        return f"Profile {self.first_name} {self.last_name}"
