from pydantic import BaseModel, Field
from typing import Optional, List
from .review import ReviewSchema
from .request import RequestSchema
from .user import UserResponseSchema


class PropertySchema(BaseModel):
    id: Optional[int] = Field(default=None)
    title: str
    price: int
    numOfRooms: int
    numOfBathrooms: int
    location: str
    imageUrl: Optional[str] = None
    


    reviews: List[ReviewSchema] = []
    requests: List[RequestSchema] = []
    user: UserResponseSchema

    class Config:
        orm_mode = True


class PropertyCreateSchema(BaseModel):
        title: str
        price: int
        numOfRooms: int
        numOfBathrooms: int
        location: str 
        imageUrl: Optional[str] = None



