from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from .base import BaseModel
from .notification import NotificationModel


class RequestModel(BaseModel):

    __tablename__ = "requests"

    id = Column(Integer, primary_key=True, index=True)

    # Columens For Request Table
    approval = Column(Boolean)

    # Foreign Keys
    user_id = Column(Integer, ForeignKey('users.id'))
    property_id = Column(Integer, ForeignKey('properties.id'), nullable=False)
    notification_id = Column(Integer, ForeignKey('notifications.id'))

    # Relationships
    user = relationship('UserModel', back_populates="requests")
    property = relationship('PropertyModel', back_populates="requests")
    notification = relationship('NotificationModel', back_populates='request')
    
    
   



