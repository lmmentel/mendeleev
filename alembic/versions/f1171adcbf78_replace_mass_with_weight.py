"""replace mass with weight

Revision ID: f1171adcbf78
Revises: 1cb409ebf667
Create Date: 2016-12-07 23:45:16.479886

"""

# revision identifiers, used by Alembic.
revision = 'f1171adcbf78'
down_revision = '1cb409ebf667'
branch_labels = None
depends_on = None

from alembic import op
import sqlalchemy as sa


def upgrade():

    with op.batch_alter_table("elements") as batch_op:
        batch_op.drop_column('mass')

    op.add_column('elements', sa.Column('atomic_weight', sa.Float))
    op.add_column('elements', sa.Column('atomic_weight_uncertainty', sa.Float))


def downgrade():

    op.add_column('elements', sa.Column('mass', sa.Float))
    with op.batch_alter_table("elements") as batch_op:
        batch_op.drop_column('atomic_weight')
        batch_op.drop_column('atomic_weight_uncertainty')
