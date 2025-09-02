from sqlalchemy import Column, Integer, String, Boolean, ForeignKey, Float
from sqlalchemy.orm import relationship
from .base import BaseModel
from sqlalchemy.dialects.postgresql import JSON



class PropertyModel(BaseModel):
    __tablename__ = "properties"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    price = Column(Integer)
    numOfRooms = Column(Integer)
    numOfBathrooms = Column(Integer)
    location = Column(String)

    images = Column(JSON, nullable=True)  # store list of URLs
    latitude = Column(Float, nullable=True)
    longitude = Column(Float, nullable=True)



    # Foreign keys
    user_id = Column(Integer, ForeignKey("users.id"))
    category_id = Column(Integer, ForeignKey("categories.id"))

    # Relationships
    user = relationship("UserModel", back_populates="properties")
    reviews = relationship("ReviewModel", back_populates="property")
    requests = relationship("RequestModel", back_populates="property")
    category = relationship("CategoryModel", back_populates="properties")
