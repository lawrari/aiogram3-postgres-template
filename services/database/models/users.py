from typing import Optional

from sqlalchemy import String
from sqlalchemy import text, BIGINT
from sqlalchemy.orm import Mapped, relationship
from sqlalchemy.orm import mapped_column

from .base import Base, TimestampMixin, TableNameMixin


class User(Base, TimestampMixin, TableNameMixin):
    user_id: Mapped[int] = mapped_column(BIGINT, primary_key=True, autoincrement=True)
    telegram_id: Mapped[int] = mapped_column(BIGINT, unique=True)
    username: Mapped[Optional[str]] = mapped_column(String(128))
    full_name: Mapped[str] = mapped_column(String(128))
    language: Mapped[str] = mapped_column(String(10), server_default=text("'en'"))

    profile: Mapped['Profile'] = relationship('Profile', back_populates='users', lazy='selectin')

    def __repr__(self):
        return f"<{self.user_id} {self.username}>"
