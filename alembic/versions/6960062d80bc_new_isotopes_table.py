"""new isotopes table

Revision ID: 6960062d80bc
Revises: b4939e81ef55
Create Date: 2022-09-25 23:31:28.858332

"""

# revision identifiers, used by Alembic.
revision = '6960062d80bc'
down_revision = 'b4939e81ef55'
branch_labels = None
depends_on = None

from alembic import op
import sqlalchemy as sa


def upgrade():

    op.add_column("isotopes", sa.Column("parity", sa.String))
    op.add_column("isotopes", sa.Column("discovery_year", sa.Integer))
    op.add_column("isotopes", sa.Column("g_factor_uncertainty", sa.Float))
    op.add_column("isotopes", sa.Column("abundance_uncertainty", sa.Float))
    op.add_column("isotopes", sa.Column("half_life_uncertainty", sa.Float))
    op.add_column("isotopes", sa.Column("quadrupole_moment_uncertainty", sa.Float))

    with op.batch_alter_table("isotopes") as batch_op:
        batch_op.alter_column("spin", type_=sa.String)


def downgrade():

    with op.batch_alter_table("isotopes") as batch_op:
        batch_op.drop_column("parity")
        batch_op.drop_column("discovery_year")
        batch_op.drop_column("g_factor_uncertainty")
        batch_op.drop_column("abundance_uncertainty")
        batch_op.drop_column("half_life_uncertainty")
        batch_op.drop_column("quadrupole_moment_uncertainty")
        batch_op.alter_column("spin", type_=sa.Float)