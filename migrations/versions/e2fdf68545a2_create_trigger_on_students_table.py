"""Create trigger on students table

Revision ID: e2fdf68545a2
Revises: 710bef23864e
Create Date: 2024-11-12 10:31:50.137326

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'e2fdf68545a2'
down_revision: Union[str, None] = '710bef23864e'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.execute(sa.DDL(
        """
        CREATE OR REPLACE FUNCTION function_set_create_at() 
            RETURNS TRIGGER AS $$
            BEGIN
                IF NEW.create_at IS NULL THEN
                    NEW.create_at = NOW();
                END IF;

                RETURN NEW;
            END;
            $$ LANGUAGE plpgsql;
        """        
    ))

    op.execute(sa.DDL(
        """
        CREATE TRIGGER trigger_set_create_at
            BEFORE INSERT or UPDATE ON students
            FOR EACH ROW 
            EXECUTE PROCEDURE function_set_create_at();
        """
    ))


def downgrade() -> None:
    op.execute(sa.DDL("DROP TRIGGER trigger_set_create_at ON students;"))
    op.execute(sa.DDL("DROP FUNCTION function_set_create_at()"))
