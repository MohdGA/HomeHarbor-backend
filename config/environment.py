import os

# Replace the postgres:// prefix from Heroku with postgresql://
db_URI = os.getenv("DATABASE_URL", "postgresql://mohd:123@localhost:5432/homeharbor")
db_URI = db_URI.replace("postgres://", "postgresql://")

DATABASE_URL = db_URI
jwt_secret = os.getenv("JWT_SECRET")
APP_ENV = os.getenv("APP_ENV", "development")
