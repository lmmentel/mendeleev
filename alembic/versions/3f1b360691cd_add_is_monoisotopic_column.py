"""add is monoisotopic column

Revision ID: 3f1b360691cd
Revises: f1171adcbf78
Create Date: 2016-12-08 00:44:07.210883

"""

# revision identifiers, used by Alembic.
revision = "3f1b360691cd"
down_revision = "f1171adcbf78"
branch_labels = None
depends_on = None

from alembic import op
import sqlalchemy as sa


def upgrade():

    op.add_column("elements", sa.Column("is_monoisotopic", sa.Boolean))


def downgrade():

    with op.batch_alter_table("elements") as batch_op:
        batch_op.drop_column("is_monoisotopic")
