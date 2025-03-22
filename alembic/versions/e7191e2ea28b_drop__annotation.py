"""drop _annotation

Revision ID: e7191e2ea28b
Revises: 285dd74e23de
Create Date: 2025-03-22 18:56:26.410019

"""

# revision identifiers, used by Alembic.
revision = 'e7191e2ea28b'
down_revision = '285dd74e23de'
branch_labels = None
depends_on = None

from alembic import op
import sqlalchemy as sa


def upgrade():
    with op.batch_alter_table("elements") as batch_op:
        batch_op.drop_column("_annotation")

def downgrade():
    pass
