"""add cas

Revision ID: 5c02f2f7171d
Revises: 121ee2bd0610
Create Date: 2017-02-09 01:25:17.155989

"""

# revision identifiers, used by Alembic.
revision = "5c02f2f7171d"
down_revision = "121ee2bd0610"
branch_labels = None
depends_on = None

from alembic import op
import sqlalchemy as sa


def upgrade():

    op.add_column("elements", sa.Column("cas", sa.String))


def downgrade():

    with op.batch_alter_table("elements") as batch_op:
        batch_op.drop_column("cas")
