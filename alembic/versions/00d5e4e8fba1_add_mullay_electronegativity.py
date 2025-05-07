"""add mullay electronegativity

Revision ID: 00d5e4e8fba1
Revises: e7191e2ea28b
Create Date: 2025-05-06 22:09:42.080695

"""

# revision identifiers, used by Alembic.
revision = '00d5e4e8fba1'
down_revision = 'e7191e2ea28b'
branch_labels = None
depends_on = None

from alembic import op
import sqlalchemy as sa


def upgrade():
    with op.batch_alter_table("elements") as batch_op:
        batch_op.add_column(sa.Column("en_mullay", sa.Float))


def downgrade():
    with op.batch_alter_table("elements") as batch_op:
        batch_op.drop_column("en_mullay")