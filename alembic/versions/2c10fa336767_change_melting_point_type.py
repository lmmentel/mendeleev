"""change melting point type

Revision ID: 2c10fa336767
Revises: 59743e288bf2
Create Date: 2015-10-22 14:08:54.892567

"""

# revision identifiers, used by Alembic.
revision = "2c10fa336767"
down_revision = "59743e288bf2"
branch_labels = None
depends_on = None

from alembic import op
import sqlalchemy as sa


def upgrade():

    with op.batch_alter_table("elements") as batch_op:
        batch_op.alter_column("melting_point", type_=sa.Float)


def downgrade():

    with op.batch_alter_table("elements") as batch_op:
        batch_op.alter_column("melting_point", type_=sa.String)
