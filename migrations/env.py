import os
from logging.config import fileConfig

from sqlalchemy import engine_from_config, pool
from alembic import context

# -------------------------
# Load environment variables
# -------------------------
from dotenv import load_dotenv
load_dotenv()  # Load .env file

# -------------------------
# Alembic Config
# -------------------------
config = context.config

# -------------------------
# Set the database URL safely
# -------------------------
db_URI = os.getenv("DB_URI")  # Make sure your .env has DB_URI
if not db_URI:
    raise ValueError("DB_URI environment variable not set!")

# Replace 'postgres://' with 'postgresql://' for SQLAlchemy compatibility
if db_URI.startswith("postgres://"):
    db_URI = db_URI.replace("postgres://", "postgresql://", 1)

config.set_main_option("sqlalchemy.url", db_URI)

# -------------------------
# Logging setup
# -------------------------
if config.config_file_name is not None:
    fileConfig(config.config_file_name)

# -------------------------
# Import models and set metadata for autogenerate
# -------------------------
import models
from models.base import Base
from models.user import UserModel
from models.property import PropertyModel
from models.review import ReviewModel
from models.request import RequestModel
from models.notification import NotificationModel
from models.category import CategoryModel

target_metadata = Base.metadata

# -------------------------
# Migration functions
# -------------------------
def run_migrations_offline() -> None:
    """Run migrations in 'offline' mode."""
    url = config.get_main_option("sqlalchemy.url")
    context.configure(
        url=url,
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
    )

    with context.begin_transaction():
        context.run_migrations()


def run_migrations_online() -> None:
    """Run migrations in 'online' mode."""
    connectable = engine_from_config(
        config.get_section(config.config_ini_section, {}),
        prefix="sqlalchemy.",
        poolclass=pool.NullPool,
    )

    with connectable.connect() as connection:
        context.configure(
            connection=connection,
            target_metadata=target_metadata,
        )
        with context.begin_transaction():
            context.run_migrations()


# -------------------------
# Execute migrations online
# -------------------------
run_migrations_online()
