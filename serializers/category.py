from pydantic import BaseModel, Field
from typing import Optional, List


class CategorySchema(BaseModel):
    id: Optional[int] = Field(default=None)
    name: str

    class Config:
        from_attributes = True  # بدل orm_mode في Pydantic v2


class CategoryCreateSchema(BaseModel):
    name: str
