"""add is_radioactive

Revision ID: a5189c25d85e
Revises: 3f1b360691cd
Create Date: 2017-01-01 20:23:44.443398

"""

# revision identifiers, used by Alembic.
revision = 'a5189c25d85e'
down_revision = '3f1b360691cd'
branch_labels = None
depends_on = None

from alembic import op
import sqlalchemy as sa


def upgrade():

    op.add_column('elements', sa.Column('is_radioactive', sa.Boolean))


def downgrade():

    with op.batch_alter_table("elements") as batch_op:
        batch_op.drop_column('is_radioactive')
