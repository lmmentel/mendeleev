"""add mendeleev number

Revision ID: 07dec3c19f1a
Revises: 4cd9c1a13771
Create Date: 2018-06-30 21:32:00.940401

"""

# revision identifiers, used by Alembic.
revision = "07dec3c19f1a"
down_revision = "4cd9c1a13771"
branch_labels = None
depends_on = None

from alembic import op
import sqlalchemy as sa


def upgrade():

    op.add_column("elements", sa.Column("mendeleev_number", sa.Integer))


def downgrade():

    with op.batch_alter_table("elements") as batch_op:
        batch_op.drop_column("mendeleev_number")
