"""add atomic radius rahm

Revision ID: 7be81742f7b9
Revises: 5c02f2f7171d
Create Date: 2017-02-09 20:41:56.175949

"""

# revision identifiers, used by Alembic.
revision = "7be81742f7b9"
down_revision = "5c02f2f7171d"
branch_labels = None
depends_on = None

from alembic import op
import sqlalchemy as sa


def upgrade():

    op.add_column("elements", sa.Column("atomic_radius_rahm", sa.Float))


def downgrade():

    with op.batch_alter_table("elements") as batch_op:
        batch_op.drop_column("atomic_radius_rahm")
