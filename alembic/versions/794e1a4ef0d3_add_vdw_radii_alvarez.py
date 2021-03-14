"""add vdw radii alvarez

Revision ID: 794e1a4ef0d3
Revises: 4fcf211b2c3a
Create Date: 2016-10-18 10:56:56.522506

"""

# revision identifiers, used by Alembic.
revision = "794e1a4ef0d3"
down_revision = "4fcf211b2c3a"
branch_labels = None
depends_on = None

from alembic import op
import sqlalchemy as sa


def upgrade():

    op.add_column("elements", sa.Column("vdw_radius_alvarez", sa.Float))


def downgrade():

    op.drop_column("elements", "vdw_radius_alvarez")
