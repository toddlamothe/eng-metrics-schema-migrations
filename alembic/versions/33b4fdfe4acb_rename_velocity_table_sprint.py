"""Rename velocity table sprint

Revision ID: 33b4fdfe4acb
Revises: 17db76e3678c
Create Date: 2021-11-26 15:55:03.875045

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '33b4fdfe4acb'
down_revision = '17db76e3678c'
branch_labels = None
depends_on = None
old_name="velocity"
new_name="sprint"


def upgrade():
    op.rename_table(old_name, new_name)


def downgrade():
    op.rename_table(new_name, old_name)
