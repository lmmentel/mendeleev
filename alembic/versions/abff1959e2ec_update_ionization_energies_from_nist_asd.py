"""update ionization energies from NIST ASD

Revision ID: abff1959e2ec
Revises: 68c046f6983b
Create Date: 2024-10-19 22:04:43.951355

"""

# revision identifiers, used by Alembic.
revision = 'abff1959e2ec'
down_revision = '68c046f6983b'
branch_labels = None
depends_on = None

from alembic import op
import sqlalchemy as sa


def upgrade():
    # drop the existing table since all data will be updated
    op.drop_table('ionizationenergies')

    # Create the new table with the specified columns
    op.create_table(
        'ionizationenergies',
        sa.Column("id", sa.Integer, primary_key=True),
        sa.Column('atomic_number', sa.Integer(), nullable=False),
        sa.Column('species_name', sa.String(), nullable=False),
        sa.Column('ion_charge', sa.Integer(), nullable=False),
        sa.Column('isoelectonic_sequence', sa.String(), nullable=False),
        sa.Column('ground_shells', sa.String(), nullable=True),
        sa.Column('ground_configuration', sa.String(), nullable=True),
        sa.Column('ground_level', sa.String(), nullable=True),
        sa.Column('ionized_level', sa.String(), nullable=True),
        sa.Column('ionization_energy', sa.Float(), nullable=True),
        sa.Column('uncertainty', sa.Float(), nullable=True),
        sa.Column('references', sa.Text(), nullable=True),
        sa.Column('is_semi_empirical', sa.Boolean(), nullable=True),
        sa.Column('is_theoretical', sa.Boolean(), nullable=True),
    )

def downgrade():
    pass
