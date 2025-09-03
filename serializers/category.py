from pydantic import BaseModel, Field
from typing import Optional, List


class CategorySchema(BaseModel):
    id: Optional[int] = Field(default=None)
    name: str

    class Config:
        from_attributes = True  


class CategoryCreateSchema(BaseModel):
    name: str
