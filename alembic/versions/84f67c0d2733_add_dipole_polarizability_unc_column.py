"""add dipole_polarizability_unc column

Revision ID: 84f67c0d2733
Revises: 07dec3c19f1a
Create Date: 2019-03-17 19:20:17.426746

"""

# revision identifiers, used by Alembic.
revision = "84f67c0d2733"
down_revision = "07dec3c19f1a"
branch_labels = None
depends_on = None

from alembic import op
import sqlalchemy as sa


def upgrade():

    op.add_column("elements", sa.Column("dipole_polarizability_unc", sa.Float))


def downgrade():

    with op.batch_alter_table("elements") as batch_op:
        batch_op.drop_column("dipole_polarizability_unc")
