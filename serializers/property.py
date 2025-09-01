from pydantic import BaseModel, Field
from typing import Optional, List
from .review import ReviewSchema
from .request import RequestSchema
from .user import UserResponseSchema
from .category import CategorySchema


class PropertySchema(BaseModel):
    id: Optional[int] = Field(default=None)
    title: str
    price: int
    numOfRooms: int
    numOfBathrooms: int
    location: str

    reviews: List[ReviewSchema] = []
    requests: List[RequestSchema] = []
    user: UserResponseSchema
    category: Optional[CategorySchema] = None

    class Config:
        from_attributes = True


class PropertyCreateSchema(BaseModel):
    title: str
    price: int
    numOfRooms: int
    numOfBathrooms: int
    location: str
    category_id: Optional[int] = None
