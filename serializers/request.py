from typing import Optional, List
from pydantic import BaseModel, Field
from .user import UserResponseSchema
from .notification import NotificationSchema
class RequestSchema(BaseModel):
   id: Optional[int] = Field(default=None)
   approval: bool
   notification: NotificationSchema
  
  
  

   class Config:
      orm_mode = True

class RequestCreateSchema(BaseModel):
   approval: bool
   
      