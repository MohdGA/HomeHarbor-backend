from pydantic import BaseModel

class NotificationSchema(BaseModel):
    id: int
    seen: bool
    request_id: int
    
    property_id: int

    class Config:
        orm_mode = True
