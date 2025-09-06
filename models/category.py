from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from .base import Base, BaseModel


class CategoryModel(Base, BaseModel):
    __tablename__ = "categories"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, nullable=False)

    
    properties = relationship("PropertyModel", back_populates="category")
