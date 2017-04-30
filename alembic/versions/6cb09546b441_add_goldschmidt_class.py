"""add goldschmidt class

Revision ID: 6cb09546b441
Revises: 769f69a5386c
Create Date: 2017-04-30 18:17:44.328447

"""

# revision identifiers, used by Alembic.
revision = '6cb09546b441'
down_revision = '769f69a5386c'
branch_labels = None
depends_on = None

from alembic import op
import sqlalchemy as sa


def upgrade():

    op.add_column('elements', sa.Column('goldschmidt_class', sa.String))


def downgrade():

    with op.batch_alter_table("elements") as batch_op:
        batch_op.drop_column('goldschmidt_class')
