from pydantic import EmailStr
from sqlalchemy.orm import Mapped, mapped_column

from app.models.base import Base

class RequestModel(Base):
    __tablename__= "requests"

    name : Mapped[str]
    phone : Mapped[str]
    email : Mapped[EmailStr]
    object_type : Mapped[str]
    service_type : Mapped[str]
    tank_size : Mapped[str]
    location : Mapped[str]
    message : Mapped[str | None] = mapped_column(default=None)