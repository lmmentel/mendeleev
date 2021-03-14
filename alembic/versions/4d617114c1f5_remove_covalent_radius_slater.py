"""remove covalent_radius_slater

Revision ID: 4d617114c1f5
Revises: 3fa9c7ae3440
Create Date: 2020-03-22 21:07:47.905796

"""

# revision identifiers, used by Alembic.
revision = "4d617114c1f5"
down_revision = "3fa9c7ae3440"
branch_labels = None
depends_on = None

from alembic import op
import sqlalchemy as sa


def upgrade():

    with op.batch_alter_table("elements") as bop:
        bop.drop_column("covalent_radius_slater")


def downgrade():
    with op.batch_alter_table("elements") as bop:
        bop.add_column(sa.Column("covalent_radius_slater", sa.Float))
