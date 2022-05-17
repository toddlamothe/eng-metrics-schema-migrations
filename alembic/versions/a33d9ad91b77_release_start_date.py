"""release start date

Revision ID: a33d9ad91b77
Revises: 8729fedb5911
Create Date: 2022-05-17 17:51:25.797718

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a33d9ad91b77'
down_revision = '8729fedb5911'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('release',
        sa.Column('start_date', sa.Date)
    )

def downgrade():
    op.drop_column('release', 'start_date')
