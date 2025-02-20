"""Merge multiple heads

Revision ID: df3ef2637403
Revises: ad2006afb66d
Create Date: 2025-02-20 13:38:33.553346

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'df3ef2637403'
down_revision: Union[str, None] = 'ad2006afb66d'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
