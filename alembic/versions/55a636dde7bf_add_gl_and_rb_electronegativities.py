"""add GL and RB electronegativities

Revision ID: 55a636dde7bf
Revises: db2973cd13af
Create Date: 2024-11-10 21:39:28.836892

"""

# revision identifiers, used by Alembic.
revision = '55a636dde7bf'
down_revision = 'db2973cd13af'
branch_labels = None
depends_on = None

from alembic import op
import sqlalchemy as sa


def upgrade():

    op.add_column("elements", sa.Column("en_gunnarsson_lundqvist", sa.Float))
    op.add_column("elements", sa.Column("en_robles_bartolotti", sa.Float))


def downgrade():

    with op.batch_alter_table("elements") as batch_op:
        batch_op.drop_column("en_gunnarsson_lundqvist")
        batch_op.drop_column("en_robles_bartolotti")