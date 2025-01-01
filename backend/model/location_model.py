from sqlalchemy import Integer
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import mapped_column, Mapped


class LocationModel(DeclarativeBase):
    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
