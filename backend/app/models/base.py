from sqlalchemy import DeclarativeBase
from sqlalchemy.orm import Mapped, mapped_column

class Base(DeclarativeBase):
    pass
    # id : Mapped[int] = mapped_column(primary_key=True)