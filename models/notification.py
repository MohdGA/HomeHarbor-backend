from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.orm import relationship

from .base import BaseModel


class NotificationModel(BaseModel):
    
    __tablename__ = "notifications"
    
    id = Column(Integer, primary_key=True, index=True)
    
    seen = Column(Boolean, default=False)
    
    # ForeignKey
    property_id = Column(Integer, ForeignKey("properties.id"), nullable=False)
    request_id = Column(Integer, ForeignKey('requests.id'), unique=True)
    
    
    # Relationship
    request = relationship('RequestModel', back_populates='notification', uselist=False)