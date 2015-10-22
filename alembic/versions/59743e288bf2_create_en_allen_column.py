"""create en allen column

Revision ID: 59743e288bf2
Revises: 239b66a4f79e
Create Date: 2015-10-22 02:27:22.333259

"""

# revision identifiers, used by Alembic.
revision = '59743e288bf2'
down_revision = '239b66a4f79e'
branch_labels = None
depends_on = None

from alembic import op
import sqlalchemy as sa


def upgrade():

    with op.batch_alter_table("elements") as batch_op:
        batch_op.add_column(sa.Column('en_allen', sa.Float))


def downgrade():

    with op.batch_alter_table("elements") as batch_op:
        batch_op.drop_column('en_allen')
