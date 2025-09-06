import os

# Pull DATABASE_URL from Heroku or DB_URI locally
db_URI = os.getenv("DATABASE_URL") or os.getenv("DB_URI")

# Fix Heroku's 'postgres://' → 'postgresql://'
if db_URI and db_URI.startswith("postgres://"):
    db_URI = db_URI.replace("postgres://", "postgresql://", 1)

jwt_secret = os.getenv("JWT_SECRET")
APP_ENV = os.getenv("APP_ENV", "development")

