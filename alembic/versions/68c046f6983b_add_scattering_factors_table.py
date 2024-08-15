"""add scattering factors table

Revision ID: 68c046f6983b
Revises: 7d745d77a7c1
Create Date: 2024-08-15 20:21:40.641912

"""

# revision identifiers, used by Alembic.
revision = '68c046f6983b'
down_revision = '7d745d77a7c1'
branch_labels = None
depends_on = None

from alembic import op
import sqlalchemy as sa


def upgrade():
    op.create_table(
        "scattering_factors",
        sa.Column("id", sa.Integer, primary_key=True),
        sa.Column("atomic_number", sa.Integer),
        sa.Column("energy", sa.Float),
        sa.Column("f1", sa.Float),
        sa.Column("f2", sa.Float),
    )


def downgrade():
    op.drop_table("scattering_factors")
