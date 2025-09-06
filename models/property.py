from sqlalchemy import Column, Integer, String, Boolean, ForeignKey, Float
from sqlalchemy.orm import relationship
from .base import Base, BaseModel

from sqlalchemy.dialects.postgresql import JSON



class PropertyModel(Base, BaseModel):
    __tablename__ = "properties"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    price = Column(Integer)
    numOfRooms = Column(Integer)
    numOfBathrooms = Column(Integer)
    location = Column(String)

    images = Column(JSON, nullable=True)  
    latitude = Column(Float, nullable=True)
    longitude = Column(Float, nullable=True)




    user_id = Column(Integer, ForeignKey("users.id"))
    category_id = Column(Integer, ForeignKey("categories.id"))

   
    user = relationship("UserModel", back_populates="properties")
    reviews = relationship("ReviewModel", back_populates="property")
    requests = relationship("RequestModel", back_populates="property")
    category = relationship("CategoryModel", back_populates="properties")
