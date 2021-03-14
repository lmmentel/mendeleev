"""add glawe number column

Revision ID: 08ca43d1d700
Revises: 6574d85399ad
Create Date: 2019-03-17 21:30:05.654265

"""

# revision identifiers, used by Alembic.
revision = "08ca43d1d700"
down_revision = "6574d85399ad"
branch_labels = None
depends_on = None

from alembic import op
import sqlalchemy as sa


def upgrade():

    op.add_column("elements", sa.Column("glawe_number", sa.Integer))


def downgrade():

    with op.batch_alter_table("elements") as batch_op:
        batch_op.drop_column("glawe_number")
