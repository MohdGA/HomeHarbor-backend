from dotenv import load_dotenv
load_dotenv()

from fastapi import FastAPI, File, UploadFile, HTTPException
from controllers.users import router as UsersRouter
from controllers.property import router as PropertyRouter
from controllers.reviews import router as ReviewRouter
from controllers.requests import router as RequestRouter
from controllers.category import router as CategoryRouter
from controllers.notification import router as NotificationRouter
from fastapi.middleware.cors import CORSMiddleware
from typing import List
import cloudinary.uploader
from config.cloudinary_config import cloudinary
from config.environment import os

app = FastAPI()


origins = [
    "http://127.0.0.1:5174",
    "http://localhost:5174",
    "http://127.0.0.1:5173",
    "http://localhost:5173",
    "https://home-harbor-frontend-x9kl-a7wz30gs4-homeharbors-projects.vercel.app"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins, 
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(UsersRouter, prefix='/api')
app.include_router(PropertyRouter, prefix='/api')
app.include_router(ReviewRouter, prefix='/api')
app.include_router(RequestRouter, prefix='/api')
app.include_router(NotificationRouter, prefix='/api')
app.include_router(CategoryRouter, prefix='/api')

@app.get('/')
def home():
    # Hello world function
    return {'message': 'Hello World!'}


@app.post("/upload/")
async def upload_images(files: List[UploadFile] = File(...)):
    urls = []
    try:
        for file in files:
            result = cloudinary.uploader.upload(file.file, folder="my_app_uploads")
            urls.append(result["secure_url"])
        return {"urls": urls}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


if os.getenv("APP_ENV", "development") != "production":
    # load .env only locally
    from dotenv import load_dotenv
    load_dotenv()