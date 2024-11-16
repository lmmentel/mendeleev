"""add supply chain attributes

Revision ID: edad0a76e11e
Revises: 55a636dde7bf
Create Date: 2024-11-12 18:24:05.169690

"""

# revision identifiers, used by Alembic.
revision = 'edad0a76e11e'
down_revision = '55a636dde7bf'
branch_labels = None
depends_on = None

from alembic import op
import sqlalchemy as sa


def upgrade():

    op.add_column("elements", sa.Column("political_stability_of_top_producer", sa.Float))
    op.add_column("elements", sa.Column("political_stability_of_top_reserve_holder", sa.Float))
    op.add_column("elements", sa.Column("production_concentration", sa.Float))
    op.add_column("elements", sa.Column("recycling_rate", sa.String))
    op.add_column("elements", sa.Column("relative_supply_risk", sa.Float))
    op.add_column("elements", sa.Column("reserve_distribution", sa.Float))
    op.add_column("elements", sa.Column("substitutability", sa.String))
    op.add_column("elements", sa.Column("top_3_producers", sa.String))
    op.add_column("elements", sa.Column("top_3_reserve_holders", sa.String))


def downgrade():

    with op.batch_alter_table("elements") as batch_op:
        batch_op.drop_column("production_concentration")
        batch_op.drop_column("relative_supply_risk")
        batch_op.drop_column("reserve_distribution")
        batch_op.drop_column("political_stability_of_top_producer")
        batch_op.drop_column("political_stability_of_top_reserve_holder")
        batch_op.drop_column("top_3_producers")
        batch_op.drop_column("top_3_reserve_holders")
        batch_op.drop_column("recycling_rate")
        batch_op.drop_column("substitutability")

