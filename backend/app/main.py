from fastapi import FastAPI

from app.api.router import api_router as router

app = FastAPI(title="Ecotech Services")

app.include_router(router, prefix="/api")



