"""create epic table

Revision ID: 84b116bbce13
Revises: 17e0cf453c00
Create Date: 2021-07-09 11:02:01.859067

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '84b116bbce13'
down_revision = '17e0cf453c00'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'epic',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('key', sa.VARCHAR(length=15), nullable=False),        
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
    op.drop_table('epic')
