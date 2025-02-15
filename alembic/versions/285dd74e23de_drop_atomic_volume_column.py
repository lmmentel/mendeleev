"""drop atomic_volume column

Revision ID: 285dd74e23de
Revises: 6b61728951ad
Create Date: 2025-02-15 22:29:46.333586

"""

# revision identifiers, used by Alembic.
revision = '285dd74e23de'
down_revision = '6b61728951ad'
branch_labels = None
depends_on = None

from alembic import op
import sqlalchemy as sa


def upgrade():
    with op.batch_alter_table("elements") as batch_op:
        batch_op.drop_column("atomic_volume")


def downgrade():
    with op.batch_alter_table("elements") as batch_op:
        batch_op.add_column("atomic_volume", sa.Float)