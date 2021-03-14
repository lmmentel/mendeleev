"""add pa and gb columns

Revision ID: 461fa3f6b545
Revises: 1e8851ab054e
Create Date: 2015-11-06 02:51:00.830043

"""

# revision identifiers, used by Alembic.
revision = "461fa3f6b545"
down_revision = "1e8851ab054e"
branch_labels = None
depends_on = None

from alembic import op
import sqlalchemy as sa


def upgrade():

    op.add_column("elements", sa.Column("proton_affinity", sa.Float))
    op.add_column("elements", sa.Column("gas_basicity", sa.Float))


def downgrade():

    op.drop_column("elements", "proton_affinity")
    op.drop_column("elements", "gas_basicity")
