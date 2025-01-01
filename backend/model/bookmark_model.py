from sqlalchemy import JSON, Integer
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import mapped_column, Mapped


class BookmarkModel(DeclarativeBase):
    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    location_list: Mapped[int] = mapped_column(JSON, primary_key=True, index=True)
