"""create phase transition table

Revision ID: e93dcf938eaf
Revises: 4bff6db401a7
Create Date: 2022-11-08 19:32:56.431200

"""

# revision identifiers, used by Alembic.
revision = "e93dcf938eaf"
down_revision = "4bff6db401a7"
branch_labels = None
depends_on = None

from alembic import op
import sqlalchemy as sa


def upgrade():
    op.create_table(
        "phasetransitions",
        sa.Column("id", sa.Integer, primary_key=True),
        sa.Column("atomic_number", sa.Integer),
        sa.Column("boiling_point", sa.Float),
        sa.Column("melting_point", sa.Float),
        sa.Column("critical_temperature", sa.Float),
        sa.Column("critical_pressure", sa.Float),
        sa.Column("triple_point_temperature", sa.Float),
        sa.Column("triple_point_pressure", sa.Float),
        sa.Column("allotrope", sa.String(50)),
    )


def downgrade():
    op.drop_table("phasetransitions")
