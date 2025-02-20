"""Final merge of Student and Faculty branches

Revision ID: 75cd2f8fd44d
Revises: df3ef2637403
Create Date: 2025-02-20 13:41:46.802603

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '75cd2f8fd44d'
down_revision: Union[str, None] = 'df3ef2637403'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
