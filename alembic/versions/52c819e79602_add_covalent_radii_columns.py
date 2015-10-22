"""add covalent radii columns

Revision ID: 52c819e79602
Revises: 
Create Date: 2015-07-27 21:17:10.656944

"""

# revision identifiers, used by Alembic.
revision = '52c819e79602'
down_revision = None
branch_labels = None
depends_on = None

from alembic import op
import sqlalchemy as sa


def upgrade():

    with op.batch_alter_table("elements") as batch_op:
        batch_op.add_column(sa.Column('covalent_radius_2008', sa.Float))
        batch_op.add_column(sa.Column('covalent_radius_2009', sa.Float))
        batch_op.drop_column('covalent_radius')

def downgrade():

    with op.batch_alter_table("elements") as batch_op:
        batch_op.drop_column('covalent_radius_2008')
        batch_op.drop_column('covalent_radius_2009')
        batch_op.add_column(sa.Column('covalent_radius', sa.Float))
