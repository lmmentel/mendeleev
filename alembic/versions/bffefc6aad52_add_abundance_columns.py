"""add abundance columns

Revision ID: bffefc6aad52
Revises: 57f0349dc312
Create Date: 2016-02-14 22:19:04.267063

"""

# revision identifiers, used by Alembic.
revision = "bffefc6aad52"
down_revision = "57f0349dc312"
branch_labels = None
depends_on = None

from alembic import op
import sqlalchemy as sa


def upgrade():

    op.add_column("elements", sa.Column("abundance_crust", sa.Float))
    op.add_column("elements", sa.Column("abundance_sea", sa.Float))


def downgrade():

    op.drop_column("elements", "abundance_crust")
    op.drop_column("elements", "abundance_sea")
