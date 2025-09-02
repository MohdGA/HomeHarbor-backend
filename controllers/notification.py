from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from models.property import PropertyModel
from models.request import RequestModel
from serializers.request import RequestSchema, RequestCreateSchema
from models.user import UserModel
from models.notification import NotificationModel
from serializers.notification import NotificationSchema

from typing import List
from database import get_db
from dependencies.get_current_user import get_current_user



router = APIRouter()

@router.get('/requests/{request_id}/notification', response_model= NotificationSchema)
def get_notifications(request_id: int, db: Session = Depends(get_db)):
    request = db.query(RequestModel).filter(RequestModel.id == request_id).first()
    
    if not request:
        raise HTTPException(status_code=404, detail="Request not found")
    
    return request.notification
    
    
    