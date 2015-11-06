"""add heat of formation column

Revision ID: 4b8324491495
Revises: 461fa3f6b545
Create Date: 2015-11-06 18:06:06.979301

"""

# revision identifiers, used by Alembic.
revision = '4b8324491495'
down_revision = '461fa3f6b545'
branch_labels = None
depends_on = None

from alembic import op
import sqlalchemy as sa


def upgrade():

    op.add_column('elements', sa.Column('heat_of_formation', sa.Float))


def downgrade():

    op.drop_column('elements', 'heat_of_formation')
