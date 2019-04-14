"""Routers package."""
from fastapi import APIRouter

from views import vehicle

api_router = APIRouter()
api_router.include_router(vehicle.router)
