"""Change FK from backlog ID to UUID

Revision ID: c624f8a079cd
Revises: 234d02c6040b
Create Date: 2021-07-10 17:46:03.855842

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c624f8a079cd'
down_revision = '234d02c6040b'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column("epic", sa.Column("backlog_uuid", sa.BINARY(16)))


def downgrade():
    op.drop_column("epic", "backlog_uuid")
