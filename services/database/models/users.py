from typing import Optional

from sqlalchemy import String
from sqlalchemy import text, BIGINT
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column

from .base import Base, TimestampMixin, TableNameMixin


class User(Base, TimestampMixin, TableNameMixin):
    """
    This class represents a User in the application.

    Attributes:
        user_id (Mapped[int]): The unique identifier of the user.
        telegram_id (Mapped[int]): The telegram id of the user.
        username (Mapped[Optional[str]]): The username of the user.
        full_name (Mapped[str]): The full name of the user.
        status (Mapped[str]): The status of the user (default, banned, restricted, etc...).
        role (Mapped[str]): The role of the user (user, admin, support, etc...).
        language (Mapped[str]): The language preference of the user.

    Methods:
        __repr__(): Returns a string representation of the User object.

    Inherited Attributes:
        Inherits from Base, TimestampMixin, and TableNameMixin classes, which provide additional attributes and functionality.

    Inherited Methods:
        Inherits methods from Base, TimestampMixin, and TableNameMixin classes, which provide additional functionality.
    """

    user_id: Mapped[int] = mapped_column(BIGINT, primary_key=True, autoincrement=True)
    telegram_id: Mapped[int] = mapped_column(BIGINT, unique=True)
    username: Mapped[Optional[str]] = mapped_column(String(128))
    full_name: Mapped[str] = mapped_column(String(128))
    status: Mapped[str] = mapped_column(String(128), server_default=text("'default'"))
    role: Mapped[str] = mapped_column(String(128), server_default=text("'user'"))
    language: Mapped[str] = mapped_column(String(10), server_default=text("'en'"))

    def __repr__(self):
        return f"<{self.role} {self.user_id} {self.username} {self.full_name}>"
