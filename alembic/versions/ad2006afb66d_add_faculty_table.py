"""Add Faculty table

Revision ID: ad2006afb66d
Revises: 0e407ee70bc2
Create Date: 2025-02-20 13:32:19.673302
"""

from typing import Sequence, Union
from alembic import op
import sqlalchemy as sa

# Revision identifiers, used by Alembic.
revision: str = 'ad2006afb66d'
down_revision: Union[str, None] = '0e407ee70bc2'  # Ensure correct migration order
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None  # Remove conflicting dependency


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
