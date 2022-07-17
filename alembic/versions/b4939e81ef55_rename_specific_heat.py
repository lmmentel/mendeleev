"""rename specific heat

Revision ID: b4939e81ef55
Revises: 615cc0829a54
Create Date: 2022-07-17 12:47:52.822701

"""

# revision identifiers, used by Alembic.
revision = 'b4939e81ef55'
down_revision = '615cc0829a54'
branch_labels = None
depends_on = None

from alembic import op
import sqlalchemy as sa


def upgrade():

    with op.batch_alter_table("elements") as bop:
        bop.alter_column(
            "specific_heat", new_column_name="specific_heat_capacity"
        )


def downgrade():

    with op.batch_alter_table("elements") as bop:
        bop.alter_column(
            "specific_heat_capacity", new_column_name="specific_heat"
        )