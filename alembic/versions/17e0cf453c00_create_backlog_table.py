"""create backlog table

Revision ID: 17e0cf453c00
Revises: 
Create Date: 2021-07-09 10:20:45.916263

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '17e0cf453c00'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'backlog',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('name', sa.VARCHAR(length=100), nullable=False),        
        sa.Column('epic_count', sa.Integer, nullable=False),        
        sa.Column('total_points', sa.Integer, nullable=False),        
        sa.Column('points_done', sa.Integer, nullable=False),      
        sa.Column('points_in_progress', sa.Integer, nullable=False),       
        sa.Column('points_to_do', sa.Integer, nullable=False),
        sa.Column('points_percent_complete', sa.Float, nullable=False),
        sa.Column('total_issues', sa.Integer, nullable=False),
        sa.Column('issues_done', sa.Integer, nullable=False),
        sa.Column('issues_in_progress', sa.Integer, nullable=False),
        sa.Column('issues_to_do', sa.Integer, nullable=False),
        sa.Column('issues_unestimated', sa.Integer, nullable=False),
        sa.Column('issues_percent_complete', sa.Float, nullable=False)        
    )


def downgrade():
    op.drop_table('backlog')
