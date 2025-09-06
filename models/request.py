from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from .base import Base, BaseModel

class RequestModel(Base,BaseModel):

    __tablename__ = "requests"

    id = Column(Integer, primary_key=True, index=True)

  
    approval = Column(Boolean)

  
    user_id = Column(Integer, ForeignKey('users.id'))
    property_id = Column(Integer, ForeignKey('properties.id'), nullable=False)

    
    user = relationship('UserModel', back_populates="requests")
    property = relationship('PropertyModel', back_populates="requests")
    notification = relationship('NotificationModel', back_populates='request', uselist=False)
    
    
   



