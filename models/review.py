from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from .base import Base, BaseModel

class ReviewModel(Base, BaseModel):
    __tablename__ = 'reviews'

  
    id = Column(Integer, primary_key=True, index=True)
    content = Column(String, nullable=False)

    #relationship
    property_id = Column(Integer, ForeignKey('properties.id'), nullable=False)
    property = relationship("PropertyModel", back_populates="reviews")

