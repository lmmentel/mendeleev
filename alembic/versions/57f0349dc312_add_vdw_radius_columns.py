"""add vdw radius columns

Revision ID: 57f0349dc312
Revises: 57be8c42cb8
Create Date: 2016-01-27 14:28:27.211275

"""

# revision identifiers, used by Alembic.
revision = '57f0349dc312'
down_revision = '57be8c42cb8'
branch_labels = None
depends_on = None

from alembic import op
import sqlalchemy as sa


def upgrade():

    op.add_column('elements', sa.Column('vdw_radius_bondi', sa.Float))
    op.add_column('elements', sa.Column('vdw_radius_truhlar', sa.Float))
    op.add_column('elements', sa.Column('vdw_radius_rt', sa.Float))
    op.add_column('elements', sa.Column('vdw_radius_batsanov', sa.Float))
    op.add_column('elements', sa.Column('vdw_radius_dreiding', sa.Float))
    op.add_column('elements', sa.Column('vdw_radius_uff', sa.Float))
    op.add_column('elements', sa.Column('vdw_radius_mm3', sa.Float))

def downgrade():

    op.drop_column('elements', 'vdw_radius_bondi')
    op.drop_column('elements', 'vdw_radius_truhlar')
    op.drop_column('elements', 'vdw_radius_rt')
    op.drop_column('elements', 'vdw_radius_batsanov')
    op.drop_column('elements', 'vdw_radius_dreiding')
    op.drop_column('elements', 'vdw_radius_uff')
    op.drop_column('elements', 'vdw_radius_mm3')
