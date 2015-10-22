"""rename electronegativity

Revision ID: 239b66a4f79e
Revises: 52c819e79602
Create Date: 2015-10-22 02:23:50.370643

"""

# revision identifiers, used by Alembic.
revision = '239b66a4f79e'
down_revision = '52c819e79602'
branch_labels = None
depends_on = None

from alembic import op
import sqlalchemy as sa


def upgrade():

    with op.batch_alter_table("elements") as batch_op:
        batch_op.add_column(sa.Column('en_pauling', sa.Float))
        batch_op.drop_column('electronegativity')

def downgrade():

    with op.batch_alter_table("elements") as batch_op:
        batch_op.add_column(sa.Column('electronegativity', sa.Float))
        batch_op.drop_column('en_pauling')
