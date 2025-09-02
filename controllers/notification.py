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
    
    
@router.put("/notifications/{notification_id}/seen", response_model=NotificationSchema)
def mark_notification_seen(notification_id: int, db: Session = Depends(get_db)):
    notification = db.query(NotificationModel).filter(NotificationModel.id == notification_id).first()
    
    if not notification:
        raise HTTPException(status_code=404, detail="Notification not found")
    
    notification.seen = True
    db.commit()
    db.refresh(notification)
    
    return notification