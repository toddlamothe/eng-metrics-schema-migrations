"""create velocity table

Revision ID: e2ad3eb0db98
Revises: 234d02c6040b
Create Date: 2021-08-19 16:37:41.823345

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e2ad3eb0db98'
down_revision = '234d02c6040b'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'velocity',
        sa.Column('backlog_id', sa.Integer, primary_key=True),
        sa.Column('sprint_id', sa.Integer, primary_key=True),
        sa.Column('name', sa.VARCHAR(length=255), nullable=False),
        sa.Column('state', sa.VARCHAR(length=255), nullable=False),
        sa.Column('goal', sa.VARCHAR(length=255), nullable=False, default=''),
        sa.Column('points_estimated', sa.Integer, nullable=False),
        sa.Column('points_done', sa.Integer, nullable=False),
        sa.Column('created_dttm', sa.DateTime, nullable=False)
    )

def downgrade():
    op.drop_table('velocity')
