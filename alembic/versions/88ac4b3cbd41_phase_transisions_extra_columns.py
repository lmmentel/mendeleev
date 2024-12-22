"""phase transisions extra columns

Revision ID: 88ac4b3cbd41
Revises: edad0a76e11e
Create Date: 2024-12-22 15:42:17.215685

"""

# revision identifiers, used by Alembic.
revision = '88ac4b3cbd41'
down_revision = 'edad0a76e11e'
branch_labels = None
depends_on = None

from alembic import op
import sqlalchemy as sa


def upgrade():
    op.add_column("phasetransitions", sa.Column("is_sublimation_point", sa.Boolean))
    op.add_column("phasetransitions", sa.Column("is_transition", sa.Boolean))


def downgrade():
    with op.batch_alter_table("phasetransitions") as batch_op:
        batch_op.drop_column("is_sublimation_point")
        batch_op.drop_column("is_transition")
