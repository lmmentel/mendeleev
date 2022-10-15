"""add isotope decay mode

Revision ID: 4bff6db401a7
Revises: 93964245e992
Create Date: 2022-10-15 19:50:00.875357

"""

# revision identifiers, used by Alembic.
revision = "4bff6db401a7"
down_revision = "93964245e992"
branch_labels = None
depends_on = None

from alembic import op
import sqlalchemy as sa


def upgrade():
    op.create_table(
        "isotopedecaymodes",
        sa.Column("id", sa.Integer, primary_key=True),
        sa.Column("isotope_id", sa.Integer(), nullable=False),
        sa.Column("mode", sa.String(10), nullable=False),
        sa.Column("relation", sa.String(1)),
        sa.Column("intensity", sa.Float(), nullable=True),
        sa.Column("is_allowed_not_observed", sa.Boolean()),
        sa.Column("is_observed_intensity_unknown", sa.Boolean()),
        sa.ForeignKeyConstraint(['isotope_id'], ['isotopes.id'], name='fk_isotope_decaymodes_1', ondelete='CASCADE'),
    )


def downgrade():
    op.drop_table("isotopedecaymodes")
