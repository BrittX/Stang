"""Location schema."""
from pydantic import BaseModel, Schema

__all__ = ("Location",)


class Location(BaseModel):
    """The definition of the location schema.
    """
    city: str = Schema(
        ...,
        description="The city where the vehicle is located"
    )
    state: str = Schema(
        ...,
        description="The state where the vehicle is located"
    )
    country: str = Schema(
        ...,
        description="The country where the vehicle is located"
    )
    zipcode: int = Schema(
        ...,
        description="The zipcode corresponding to the location of the vehicle.",
    )
