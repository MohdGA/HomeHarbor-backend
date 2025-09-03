import os

db_URI = os.getenv("DB_URI")
DATABASE_URL = os.getenv(db_URI)
jwt_secret = os.getenv("JWT_SECRET")
