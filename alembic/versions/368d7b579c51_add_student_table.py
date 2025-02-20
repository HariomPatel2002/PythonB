"""Add Student table

Revision ID: 368d7b579c51
Revises: 0e407ee70bc2
Create Date: 2025-02-20 13:29:01.485656

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '368d7b579c51'
down_revision: Union[str, None] = '0e407ee70bc2'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = '0e407ee70bc2'


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
