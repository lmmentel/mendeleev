"""add c6 column

Revision ID: 5cc7e8b21b
Revises: 4b8324491495
Create Date: 2015-11-28 19:41:29.197572

"""

# revision identifiers, used by Alembic.
revision = '5cc7e8b21b'
down_revision = '4b8324491495'
branch_labels = None
depends_on = None

from alembic import op
import sqlalchemy as sa


def upgrade():

    op.add_column('elements', sa.Column('c6', sa.Float))

def downgrade():

    op.drop_column('elements', 'c6')
