from fastapi import APIRouter
from app.api.routes.requests import router as request_router

api_router =  APIRouter()

api_router.include_router(request_router, prefix="/v1")