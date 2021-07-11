"""Create backlog and epic tables

Revision ID: 234d02c6040b
Revises: 
Create Date: 2021-07-10 08:33:47.849645

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '234d02c6040b'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():

    op.create_table(
        'backlog',
        sa.Column('uuid', sa.VARCHAR(255), primary_key=True),
        sa.Column('backlog_id', sa.Integer, nullable=False),
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
        sa.Column('issues_percent_complete', sa.Float, nullable=False),
        sa.Column('created_dttm', sa.DateTime, nullable=False)
    )

    op.create_table(
        'epic',
        sa.Column('uuid', sa.VARCHAR(255), primary_key=True),
        sa.Column('backlog_uuid', sa.VARCHAR(255), nullable=False),
        sa.Column('epic_id', sa.Integer, nullable=False),        
        sa.Column('key', sa.VARCHAR(length=15), nullable=False),        
        sa.Column('name', sa.VARCHAR(length=100), nullable=False),        
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
        sa.Column('issues_percent_complete', sa.Float, nullable=False),
        sa.Column('created_dttm', sa.DateTime, nullable=False)
    )


def downgrade():
    op.drop_table('epic')
    op.drop_table('backlog')