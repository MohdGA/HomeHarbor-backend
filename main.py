from dotenv import load_dotenv
load_dotenv()

from fastapi import FastAPI
from controllers.users import router as UsersRouter
from controllers.property import router as PropertyRouter

app = FastAPI()
app.include_router(UsersRouter, prefix='/api')
app.include_router(PropertyRouter, prefix='/api')

@app.get('/')
def home():
    # Hello world function
    return {'message': 'Hello World!'}
