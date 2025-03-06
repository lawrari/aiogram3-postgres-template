from sqlalchemy import BIGINT
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column

from .base import Base, TimestampMixin, TableNameMixin


class Profile(Base, TimestampMixin, TableNameMixin):
    profile_id: Mapped[int] = mapped_column(BIGINT, primary_key=True, autoincrement=True)

    def __repr__(self):
        return f"<Profile {self.profile_id}>"
