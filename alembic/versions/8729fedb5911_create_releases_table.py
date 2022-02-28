"""create releases table

Revision ID: 8729fedb5911
Revises: 6a107ee4a90f
Create Date: 2022-02-27 18:01:44.938403

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '8729fedb5911'
down_revision = '6a107ee4a90f'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'release',
        sa.Column('uuid', sa.VARCHAR(255), primary_key=True),
        sa.Column('is_active', sa.Boolean, primary_key=False),
        sa.Column('backlog_id', sa.Integer, primary_key=False),
        sa.Column('release_name', sa.VARCHAR(length=100), primary_key=False),
        sa.Column('release_description', sa.VARCHAR(length=255), nullable=False),
        sa.Column('epic_tag', sa.VARCHAR(length=50), nullable=False),
        sa.Column('created_dttm', sa.DateTime, nullable=False)
    )

def downgrade():
    op.drop_table('release')
