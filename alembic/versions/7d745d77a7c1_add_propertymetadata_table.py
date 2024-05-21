"""add PropertyMetadata table

Revision ID: 7d745d77a7c1
Revises: 703682715347
Create Date: 2024-05-21 13:11:24.427405

"""

# revision identifiers, used by Alembic.
revision = '7d745d77a7c1'
down_revision = '703682715347'
branch_labels = None
depends_on = None

from alembic import op
import sqlalchemy as sa


value_origin_enum = sa.Enum('STORED', 'COMPUTED', name='valueorigin')

def upgrade():
    
    op.create_table(
        'propertymetadata',
        sa.Column('id', sa.Integer, primary_key=True, autoincrement=True),
        sa.Column('table', sa.String, nullable=True),
        sa.Column('column', sa.String, nullable=True),
        sa.Column('category', sa.String, nullable=False),
        sa.Column('value_origin', value_origin_enum, nullable=False),
        sa.Column('description', sa.Text, nullable=False),
        sa.Column('unit', sa.String, nullable=True),
        sa.Column('annotations', sa.Text, nullable=True),
        sa.Column('citation_keys', sa.String, nullable=True)
    )


def downgrade():
    op.drop_table('propertymetadata')
    value_origin_enum.drop(op.get_bind())