"""add molcas gv color

Revision ID: 32c95be6f49
Revises: bffefc6aad52
Create Date: 2016-02-17 14:36:37.343313

"""

# revision identifiers, used by Alembic.
revision = "32c95be6f49"
down_revision = "bffefc6aad52"
branch_labels = None
depends_on = None

from alembic import op
import sqlalchemy as sa


def upgrade():

    op.add_column("elements", sa.Column("molcas_gv_color", sa.String))


def downgrade():

    op.drop_column("elements", "molcas_gv_color")
