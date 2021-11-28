"""Add issues table

Revision ID: 6a107ee4a90f
Revises: 33b4fdfe4acb
Create Date: 2021-11-26 16:14:14.410703

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '6a107ee4a90f'
down_revision = '33b4fdfe4acb'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'issue',
        sa.Column('issue_id', sa.Integer, primary_key=True),
        sa.Column('sprint_id', sa.Integer, primary_key=False),
        sa.Column('key', sa.VARCHAR(length=255), nullable=False),
        sa.Column('description', sa.VARCHAR(length=255), nullable=False),
        sa.Column('point_estimate', sa.VARCHAR(length=255), nullable=False, default=''),
        sa.Column('status', sa.Integer, nullable=False),
        sa.Column('created_dttm', sa.DateTime, nullable=False),
        sa.Column('resolved_dttm', sa.DateTime, nullable=False)
    )

def downgrade():
    op.drop_table('issue')