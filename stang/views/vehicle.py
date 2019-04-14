"""Vehicle views"""
from typing import List

from fastapi import APIRouter

import schemas

router = APIRouter()


@router.get("/vehicles/", tags=["vehicles"], response_model=List[schemas.Vehicle])
def list_vehicles():
    """List all of the availale vehicles."""
    return []

@router.post("/vehicles/", tags=["vehicles"], response_model=schemas.Vehicle, responses={404: {"model": schemas.Error, "description": "Invalid object"}})
def add_vehicle(vehicle: schemas.Vehicle):
    """Add in a vehicle."""
    return {}
