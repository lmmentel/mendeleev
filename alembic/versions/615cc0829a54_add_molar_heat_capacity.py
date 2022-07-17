"""add molar_heat_capacity

Revision ID: 615cc0829a54
Revises: 4d617114c1f5
Create Date: 2022-07-17 12:44:53.465229

"""

# revision identifiers, used by Alembic.
revision = '615cc0829a54'
down_revision = '4d617114c1f5'
branch_labels = None
depends_on = None

from alembic import op
import sqlalchemy as sa


def upgrade():
    
    op.add_column("elements", sa.Column("molar_heat_capacity", sa.Float))


def downgrade():

    with op.batch_alter_table("elements") as batch_op:
        batch_op.drop_column("molar_heat_capacity")
