"""Vehicle schema."""
from pydantic import BaseModel, Schema

__all__ = ("Vehicle",)


class Vehicle(BaseModel):
    make: str = Schema(
        ...,
        description="The make of the vehicle"
    )
    model: str = Schema(
        ...,
        description="The model of the vehicle"
    )
    year: int = Schema(
        ...,
        description="The year of the vehicle"
    )
    trim: str = Schema(
        ...,
        description="The trim for the make and model"
    )
    # Add validation/regex later for VINs
    vin: str = Schema(
        default="1",
        description="The VIN corresponding to the vehicle",
    )
