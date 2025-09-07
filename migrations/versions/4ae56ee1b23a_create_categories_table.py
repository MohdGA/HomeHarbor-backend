"""create categories table

Revision ID: 4ae56ee1b23a
Revises: a0856b4ae0cf
Create Date: 2025-09-07 13:12:23.773196

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '4ae56ee1b23a'
down_revision: Union[str, Sequence[str], None] = 'a0856b4ae0cf'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    pass


def downgrade() -> None:
    """Downgrade schema."""
    pass
