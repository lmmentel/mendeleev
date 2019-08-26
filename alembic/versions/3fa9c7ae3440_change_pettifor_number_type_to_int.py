"""change pettifor_number type to int

Revision ID: 3fa9c7ae3440
Revises: 08ca43d1d700
Create Date: 2019-08-26 11:08:29.867332

"""

# revision identifiers, used by Alembic.
revision = '3fa9c7ae3440'
down_revision = '08ca43d1d700'
branch_labels = None
depends_on = None

from alembic import op
import sqlalchemy as sa


def upgrade():

    with op.batch_alter_table("elements") as batch_op:
        batch_op.alter_column("pettifor_number", type_=sa.Integer)


def downgrade():

    with op.batch_alter_table("elements") as batch_op:
        batch_op.alter_column("pettifor_number", type_=sa.Float)
