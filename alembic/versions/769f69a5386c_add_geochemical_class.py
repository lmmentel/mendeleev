"""add geochemical class

Revision ID: 769f69a5386c
Revises: 7be81742f7b9
Create Date: 2017-04-30 17:37:21.761001

"""

# revision identifiers, used by Alembic.
revision = '769f69a5386c'
down_revision = '7be81742f7b9'
branch_labels = None
depends_on = None

from alembic import op
import sqlalchemy as sa


def upgrade():

    op.add_column('elements', sa.Column('geochemical_class', sa.String))


def downgrade():

    with op.batch_alter_table("elements") as batch_op:
        batch_op.drop_column('geochemical_class')
