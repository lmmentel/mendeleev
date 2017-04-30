"""add metallic radii

Revision ID: c70419b916a3
Revises: 6cb09546b441
Create Date: 2017-04-30 20:46:55.606439

"""

# revision identifiers, used by Alembic.
revision = 'c70419b916a3'
down_revision = '6cb09546b441'
branch_labels = None
depends_on = None

from alembic import op
import sqlalchemy as sa


def upgrade():

    op.add_column('elements', sa.Column('metallic_radius', sa.Float))
    op.add_column('elements', sa.Column('metallic_radius_c12', sa.Float))


def downgrade():

    with op.batch_alter_table("elements") as batch_op:
        batch_op.drop_column('metallic_radius')
        batch_op.drop_column('metallic_radius_c12')
