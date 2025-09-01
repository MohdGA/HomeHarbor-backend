from typing import Optional, List
from pydantic import BaseModel, Field
from .user import UserResponseSchema
# from .property import PropertySchema

class RequestSchema(BaseModel):
   id: Optional[int] = Field(default=None)
   approval: bool
   
   # Relationships
  
   # property: PropertySchema

   class Config:
      orm_mode = True
      