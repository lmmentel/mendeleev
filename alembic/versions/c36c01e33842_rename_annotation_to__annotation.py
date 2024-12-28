"""rename annotation to _annotation

Revision ID: c36c01e33842
Revises: 88ac4b3cbd41
Create Date: 2024-12-28 18:51:08.087363

"""

# revision identifiers, used by Alembic.
revision = 'c36c01e33842'
down_revision = '88ac4b3cbd41'
branch_labels = None
depends_on = None

from alembic import op
import sqlalchemy as sa


def upgrade():
    with op.batch_alter_table("elements") as bop:
        bop.alter_column(
            "annotation", new_column_name="_annotation"
        )


def downgrade():
    with op.batch_alter_table("elements") as bop:
        bop.alter_column(
            "_annotation", new_column_name="annotation"
        )
