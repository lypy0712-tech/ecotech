from pydantic import BaseModel, Field, EmailStr

class RequestCreateSchema(BaseModel):
    name : str
    company : str
    phone : str
    email : EmailStr
    object_type : str
    service_type : str
    tank_size : str
    location : str
    message : str | None = Field(default=None)


class RequestResponseSchema(BaseModel):
    id : int
    name : str
    company : str
    phone : str
    email : EmailStr
    object_type : str
    service_type : str
    tank_size : str
    location : str
    message : str | None = Field(default=None)