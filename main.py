from dotenv import load_dotenv
load_dotenv()

from fastapi import FastAPI, File, UploadFile, HTTPException
from controllers.users import router as UsersRouter
from controllers.property import router as PropertyRouter
from controllers.reviews import router as ReviewRouter
from controllers.requests import router as RequestRouter
from controllers.category import router as CategoryRouter
from fastapi.middleware.cors import CORSMiddleware
import cloudinary.uploader
from config.cloudinary_config import cloudinary

app = FastAPI()


origins = [
    "http://127.0.0.1:5174",
    "http://localhost:5174",
    "http://127.0.0.1:5173",
    "http://localhost:5173",
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
app.include_router(CategoryRouter, prefix='/api')

@app.get('/')
def home():
    # Hello world function
    return {'message': 'Hello World!'}


@app.post("/upload/")
async def upload_image(file: UploadFile = File(...)):
    try:
        result = cloudinary.uploader.upload(file.file, folder="my_app_uploads")
        return {"url": result["secure_url"], "public_id": result["public_id"]}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
