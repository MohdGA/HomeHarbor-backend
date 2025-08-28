from typing import Optional
from pydantic import BaseModel, Field
from .user import UserResponseSchema
from .property import PropertyResponseSchema

class RequestSchema(BaseModel):
   id: Optional[int] = Field(default=None)
   title: str
   approval: bool

   # Relationships
   user: UserResponseSchema
   property: PropertyResponseSchema



class Config:
   orm_mode = True