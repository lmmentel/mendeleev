"""add category to OxidationState

Revision ID: 93964245e992
Revises: 6960062d80bc
Create Date: 2022-09-28 13:55:33.714614

"""

# revision identifiers, used by Alembic.
revision = '93964245e992'
down_revision = '6960062d80bc'
branch_labels = None
depends_on = None

from alembic import op
import sqlalchemy as sa


def upgrade():
    op.add_column("oxidationstates", sa.Column("category", sa.String))


def downgrade():
    with op.batch_alter_table("oxidationstates") as batch_op:
        batch_op.drop_column("pettifor_number")
