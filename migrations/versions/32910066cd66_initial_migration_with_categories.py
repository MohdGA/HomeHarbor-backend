"""initial migration with categories

Revision ID: 32910066cd66
Revises: 
Create Date: 2025-09-07 14:24:16.825444

"""
from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = '32910066cd66'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    """Upgrade schema."""
    op.create_table(
        'categories',
        sa.Column('id', sa.Integer, primary_key=True, index=True),
        sa.Column('name', sa.String, unique=True, nullable=False),
    )


def downgrade() -> None:
    """Downgrade schema."""
    op.drop_table('categories')
