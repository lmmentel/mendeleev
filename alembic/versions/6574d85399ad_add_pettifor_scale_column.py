"""add pettifor scale column

Revision ID: 6574d85399ad
Revises: 84f67c0d2733
Create Date: 2019-03-17 21:13:38.242732

"""

# revision identifiers, used by Alembic.
revision = "6574d85399ad"
down_revision = "84f67c0d2733"
branch_labels = None
depends_on = None

from alembic import op
import sqlalchemy as sa


def upgrade():

    op.add_column("elements", sa.Column("pettifor_number", sa.Float))


def downgrade():

    with op.batch_alter_table("elements") as batch_op:
        batch_op.drop_column("pettifor_number")
