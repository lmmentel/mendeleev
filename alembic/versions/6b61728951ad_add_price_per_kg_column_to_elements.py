"""add price_per_kg column to elements

Revision ID: 6b61728951ad
Revises: c36c01e33842
Create Date: 2025-01-03 21:49:02.101851

"""

# revision identifiers, used by Alembic.
revision = '6b61728951ad'
down_revision = 'c36c01e33842'
branch_labels = None
depends_on = None

from alembic import op
import sqlalchemy as sa


def upgrade():
    op.add_column("elements", sa.Column("price_per_kg", sa.Float, nullable=True))


def downgrade():
    with op.batch_alter_table("elements") as batch_op:
        batch_op.drop_column("price_per_kg")
