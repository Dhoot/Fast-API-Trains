from fastapi import APIRouter

from app.api.v1 import trains

api_router = APIRouter()
api_router.include_router(trains.router, prefix="/trains", tags=["trains"])
api_router.include_router(trains.router, prefix="/daily_data", tags=["daily_data"])
