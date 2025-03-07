"""Merged Student and Faculty branches into one head

Revision ID: f81095648066
Revises: 368d7b579c51, 75cd2f8fd44d
Create Date: 2025-02-28 08:41:41.417105

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'f81095648066'
down_revision: Union[str, None] = ('368d7b579c51', '75cd2f8fd44d')
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
