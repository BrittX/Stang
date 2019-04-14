"""Error schema."""
from pydantic import BaseModel, Schema

__all__ = ("Error",)


class Error(BaseModel):
    """The definition of the error schema.
    """
    code: int = Schema(
        ...,
        description="The status code for the error"
    )
    message: str = Schema(
        ...,
        description="The message for the error"
    )
