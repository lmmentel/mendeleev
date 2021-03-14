"""add name origin sources uses

Revision ID: 4cd9c1a13771
Revises: 5a05464c07ae
Create Date: 2017-09-07 11:18:00.919996

"""

# revision identifiers, used by Alembic.
revision = "4cd9c1a13771"
down_revision = "5a05464c07ae"
branch_labels = None
depends_on = None

from alembic import op
import sqlalchemy as sa


def upgrade():

    op.add_column("elements", sa.Column("name_origin", sa.String))
    op.add_column("elements", sa.Column("sources", sa.String))
    op.add_column("elements", sa.Column("uses", sa.String))


def downgrade():

    with op.batch_alter_table("elements") as batch_op:
        batch_op.drop_column("name_origin")
        batch_op.drop_column("sources")
        batch_op.drop_column("uses")
