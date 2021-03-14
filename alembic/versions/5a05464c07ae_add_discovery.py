"""add discovery

Revision ID: 5a05464c07ae
Revises: c4a0292785e6
Create Date: 2017-09-06 21:55:21.193584

"""

# revision identifiers, used by Alembic.
revision = "5a05464c07ae"
down_revision = "c4a0292785e6"
branch_labels = None
depends_on = None

from alembic import op
import sqlalchemy as sa


def upgrade():

    op.add_column("elements", sa.Column("discoverers", sa.String))
    op.add_column("elements", sa.Column("discovery_year", sa.Integer))
    op.add_column("elements", sa.Column("discovery_location", sa.String))


def downgrade():

    with op.batch_alter_table("elements") as batch_op:
        batch_op.drop_column("discoverers")
        batch_op.drop_column("discovery_year")
        batch_op.drop_column("discovery_location")
