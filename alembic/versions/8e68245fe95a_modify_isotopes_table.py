"""modify isotopes table

Revision ID: 8e68245fe95a
Revises: a5189c25d85e
Create Date: 2017-01-07 15:11:16.650856

"""

# revision identifiers, used by Alembic.
revision = '8e68245fe95a'
down_revision = 'a5189c25d85e'
branch_labels = None
depends_on = None

from alembic import op
import sqlalchemy as sa


def upgrade():

    op.add_column('isotopes', sa.Column('mass_uncertainty', sa.Float))
    op.add_column('isotopes', sa.Column('is_radioactive', sa.Boolean))
    op.add_column('isotopes', sa.Column('half_life', sa.Float))
    op.add_column('isotopes', sa.Column('half_life_unit', sa.String))


def downgrade():

    with op.batch_alter_table('isotopes') as batch_op:
        batch_op.drop_column('mass_uncertainty')
        batch_op.drop_column('is_radioactive')
        batch_op.drop_column('half_life')
        batch_op.drop_column('half_life_unit')
