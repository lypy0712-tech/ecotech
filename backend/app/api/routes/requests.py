from fastapi import APIRouter
from app.schemas.requests import RequestCreateSchema, RequestResponseSchema

router = APIRouter(prefix="/requests", tags=["Requests"])

@router.get("")
async def get_all_requests():
    return {"message":"Get Done"}


@router.post("/add")
async def add_request(payload: RequestCreateSchema) -> RequestResponseSchema:
    return {"message":"Post Done"}