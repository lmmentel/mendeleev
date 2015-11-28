"""rename and add covalent radii

Revision ID: 57be8c42cb8
Revises: 5cc7e8b21b
Create Date: 2015-11-28 21:40:47.840359

"""

# revision identifiers, used by Alembic.
revision = '57be8c42cb8'
down_revision = '5cc7e8b21b'
branch_labels = None
depends_on = None

from alembic import op
import sqlalchemy as sa


def upgrade():

    with op.batch_alter_table('elements') as bop:
        bop.alter_column('covalent_radius_2008', new_column_name='covalent_radius_cordero')
        bop.alter_column('covalent_radius_2009', new_column_name='covalent_radius_pyykko')
        bop.add_column(sa.Column('covalent_radius_bragg', sa.Float))
        bop.add_column(sa.Column('covalent_radius_slater', sa.Float))


def downgrade():

     with op.batch_alter_table('elements') as bop:
        bop.alter_column('covalent_radius_cordero', new_column_name='covalent_radius_2008')
        bop.alter_column('covalent_radius_pyykko', new_column_name='covalent_radius_2009')
        bop.drop_column('covalent_radius_bragg')
        bop.drop_column('covalent_radius_slater')
