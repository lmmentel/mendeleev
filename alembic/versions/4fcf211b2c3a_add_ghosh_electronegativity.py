"""add ghosh electronegativity

Revision ID: 4fcf211b2c3a
Revises: 32c95be6f49
Create Date: 2016-10-16 01:05:04.752755

"""

# revision identifiers, used by Alembic.
revision = "4fcf211b2c3a"
down_revision = "32c95be6f49"
branch_labels = None
depends_on = None

from alembic import op
import sqlalchemy as sa


def upgrade():

    op.add_column("elements", sa.Column("en_ghosh", sa.Float))


def downgrade():

    op.drop_column("elements", "en_ghosh")
