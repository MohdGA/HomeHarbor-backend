from dotenv import load_dotenv
load_dotenv()

from fastapi import FastAPI
from controllers.reviews import router as ReviewsRouter


app = FastAPI()

app.include_router(ReviewsRouter, prefix='/api')


@app.get('/')
def home():
    # Hello world function
    return {'message': 'Hello World!'}
