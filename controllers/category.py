from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from models.category import CategoryModel
from database import get_db  
from serializers.category import CategorySchema, CategoryCreateSchema  

router = APIRouter()

@router.get("/", response_model=list[CategorySchema])
def get_categories(db: Session = Depends(get_db)):
    return db.query(CategoryModel).all()

@router.post("/", response_model=CategorySchema)
def create_category(category: CategoryCreateSchema, db: Session = Depends(get_db)):
    new_category = CategoryModel(name=category.name)
    db.add(new_category)
    db.commit()
    db.refresh(new_category)
    return new_category
