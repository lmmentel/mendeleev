"""add gould bucko c6 column

Revision ID: 1cb409ebf667
Revises: 794e1a4ef0d3
Create Date: 2016-10-18 12:18:27.687923

"""

# revision identifiers, used by Alembic.
revision = '1cb409ebf667'
down_revision = '794e1a4ef0d3'
branch_labels = None
depends_on = None

from alembic import op
import sqlalchemy as sa


def upgrade():

    op.add_column('elements', sa.Column('c6_gb', sa.Float))


def downgrade():

    op.drop_column('elements', 'c6_gb')
