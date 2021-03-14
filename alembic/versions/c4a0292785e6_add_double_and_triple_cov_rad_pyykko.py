"""add double and triple cov rad pyykko

Revision ID: c4a0292785e6
Revises: c70419b916a3
Create Date: 2017-06-28 16:24:40.831742

"""

# revision identifiers, used by Alembic.
revision = "c4a0292785e6"
down_revision = "c70419b916a3"
branch_labels = None
depends_on = None

from alembic import op
import sqlalchemy as sa


def upgrade():

    op.add_column("elements", sa.Column("covalent_radius_pyykko_double", sa.Float))
    op.add_column("elements", sa.Column("covalent_radius_pyykko_triple", sa.Float))


def downgrade():

    with op.batch_alter_table("elements") as batch_op:
        batch_op.drop_column("ovalent_radius_pyykko_double")
        batch_op.drop_column("covalent_radius_pyykko_triple")
