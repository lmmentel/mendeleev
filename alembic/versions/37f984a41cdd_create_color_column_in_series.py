"""create color column in series

Revision ID: 37f984a41cdd
Revises: 2c10fa336767
Create Date: 2015-10-27 15:23:46.368272

"""

# revision identifiers, used by Alembic.
revision = "37f984a41cdd"
down_revision = "2c10fa336767"
branch_labels = None
depends_on = None

from alembic import op
import sqlalchemy as sa


def upgrade():

    op.add_column("series", sa.Column("color", sa.String))


def downgrade():

    op.drop_column("series", "color")
