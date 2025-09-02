from pydantic import BaseModel

class NotificationSchema(BaseModel):
    id: int
    seen: bool
    
    
    class Config:
        orm_mode = True
