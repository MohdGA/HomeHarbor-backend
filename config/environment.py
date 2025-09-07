import os


db_URI = os.getenv('DB_URI')
DATABASE_URL = db_URI
jwt_secret = os.getenv("JWT_SECRET")
APP_ENV = os.getenv("APP_ENV", "development")
