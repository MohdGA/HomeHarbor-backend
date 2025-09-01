from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from .base import BaseModel



class PropertyModel(BaseModel):
    __tablename__ = "properties"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    price = Column(Integer)
    numOfRooms = Column(Integer)
    numOfBathrooms = Column(Integer)
    location = Column(String)

  
    imageUrl = Column(String, nullable=True)


    # Foreign keys
    user_id = Column(Integer, ForeignKey("users.id"))
    category_id = Column(Integer, ForeignKey("categories.id"))

    # Relationships
    user = relationship("UserModel", back_populates="properties")
    reviews = relationship("ReviewModel", back_populates="property")
    requests = relationship("RequestModel", back_populates="property")
    category = relationship("CategoryModel", back_populates="properties")
