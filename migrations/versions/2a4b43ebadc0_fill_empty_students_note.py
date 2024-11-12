"""Fill empty students note

Revision ID: 2a4b43ebadc0
Revises: e2fdf68545a2
Create Date: 2024-11-12 10:34:32.675734

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '2a4b43ebadc0'
down_revision: Union[str, None] = 'e2fdf68545a2'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.execute(sa.DDL(
        """
        UPDATE students
        SET    note = '<empty>'
        WHERE  note IS NULL
            OR TRIM(note) = ''; 
        """
    ))


def downgrade() -> None:
    pass
