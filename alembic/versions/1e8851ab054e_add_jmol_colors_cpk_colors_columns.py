"""add jmol colors cpk colors columns

Revision ID: 1e8851ab054e
Revises: 37f984a41cdd
Create Date: 2015-10-27 19:42:22.990188

"""

# revision identifiers, used by Alembic.
revision = "1e8851ab054e"
down_revision = "37f984a41cdd"
branch_labels = None
depends_on = None

from alembic import op
import sqlalchemy as sa


def upgrade():

    op.add_column("elements", sa.Column("jmol_color", sa.String))
    op.add_column("elements", sa.Column("cpk_color", sa.String))


def downgrade():

    op.drop_column("elements", "jmol_color")
    op.drop_column("elements", "cpk_color")
