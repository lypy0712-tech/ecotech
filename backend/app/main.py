from fastapi import FastAPI, APIRouter

from api.router import api_router as router

app = FastAPI(title="Ecotech Services")

app.include_router(router, prefix="/api")



