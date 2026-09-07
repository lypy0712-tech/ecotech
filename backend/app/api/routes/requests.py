from fastapi import APIRouter
from backend.app.schemas.requests import RequestCreateSchema, RequestResponseSchema

router = APIRouter(prefix="requests", tags=["Requests"])

@router.get("")
async def get_all_requests():
    pass


@router.post("/add")
async def add_request(payload: RequestCreateSchema) -> RequestResponseSchema:
    return RequestResponseSchema