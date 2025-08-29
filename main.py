from dotenv import load_dotenv
load_dotenv()

from fastapi import FastAPI
from controllers.users import router as UsersRouter
from controllers.property import router as PropertyRouter
from controllers.reviews import router as ReviewRouter
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()


origins = [
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

@app.get('/')
def home():
    # Hello world function
    return {'message': 'Hello World!'}
