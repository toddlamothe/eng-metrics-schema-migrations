"""Adde sprint start/end dates

Revision ID: 17db76e3678c
Revises: e2ad3eb0db98
Create Date: 2021-08-24 21:05:10.646697

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '17db76e3678c'
down_revision = 'e2ad3eb0db98'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('velocity',
        sa.Column('start_date', sa.Date)
    )
    op.add_column('velocity',
        sa.Column('end_date', sa.Date)
    )

def downgrade():
    op.drop_column('velocity', 'start_date')
    op.drop_column('velocity', 'end_date')
