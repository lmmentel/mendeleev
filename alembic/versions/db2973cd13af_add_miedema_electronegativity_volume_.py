"""add miedema electronegativity volume and density

Revision ID: db2973cd13af
Revises: abff1959e2ec
Create Date: 2024-11-05 22:29:32.441355

"""

# revision identifiers, used by Alembic.
revision = 'db2973cd13af'
down_revision = 'abff1959e2ec'
branch_labels = None
depends_on = None

from alembic import op
import sqlalchemy as sa


def upgrade():

    op.add_column("elements", sa.Column("en_miedema", sa.Float))
    op.add_column("elements", sa.Column("miedema_molar_volume", sa.Float))
    op.add_column("elements", sa.Column("miedema_electron_density", sa.Float))


def downgrade():

    with op.batch_alter_table("elements") as batch_op:
        batch_op.drop_column("en_miedema")
        batch_op.drop_column("miedema_molar_volume")
        batch_op.drop_column("miedema_electron_density")
