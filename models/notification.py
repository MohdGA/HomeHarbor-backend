from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.orm import relationship

from .base import BaseModel


class NotificationModel(BaseModel):
    
    __tablename__ = "notifications"
    
    id = Column(Integer, primary_key=True, index=True)
    seen = Column(Boolean)
    
    # ForeignKey
    
    
    # Relationship
    request = relationship('RequestModel', back_populates='request', uselist=False)