"""Add record timestamps

Revision ID: 9b129e5e8e20
Revises: 84b116bbce13
Create Date: 2021-07-09 16:00:21.031249

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9b129e5e8e20'
down_revision = '84b116bbce13'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('backlog', sa.Column('created_dttm', sa.DateTime))
    op.add_column('epic', sa.Column('created_dttm', sa.DateTime))


def downgrade():
    op.drop_column('backlog', "created_dttm")
    op.drop_column('epic', "created_dttm")
