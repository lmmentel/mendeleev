"""remove melting_point and boiling_point columns

Revision ID: 703682715347
Revises: e93dcf938eaf
Create Date: 2022-11-09 11:05:04.654668

"""

# revision identifiers, used by Alembic.
revision = "703682715347"
down_revision = "e93dcf938eaf"
branch_labels = None
depends_on = None

from alembic import op
import sqlalchemy as sa


def upgrade():
    with op.batch_alter_table("elements") as batch_op:
        batch_op.drop_column("boiling_point")
        batch_op.drop_column("melting_point")


def downgrade():
    with op.batch_alter_table("elements") as batch_op:
        batch_op.add_column("boiling_point")
        batch_op.add_column("melting_point")
