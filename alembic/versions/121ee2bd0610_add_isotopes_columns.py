"""add isotopes columns

Revision ID: 121ee2bd0610
Revises: 8e68245fe95a
Create Date: 2017-01-25 14:13:49.384000

"""

# revision identifiers, used by Alembic.
revision = "121ee2bd0610"
down_revision = "8e68245fe95a"
branch_labels = None
depends_on = None

from alembic import op
import sqlalchemy as sa


def upgrade():

    op.add_column("isotopes", sa.Column("spin", sa.Float))
    op.add_column("isotopes", sa.Column("g_factor", sa.Float))
    op.add_column("isotopes", sa.Column("quadrupole_moment", sa.Float))


def downgrade():

    with op.batch_alter_table("isotopes") as batch_op:
        batch_op.drop_column("spin")
        batch_op.drop_column("g_factor")
        batch_op.drop_column("quadrupole_moment")
