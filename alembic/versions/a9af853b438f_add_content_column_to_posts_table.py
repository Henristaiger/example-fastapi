"""add content column to posts table

Revision ID: a9af853b438f
Revises: 67f5508094e3
Create Date: 2022-10-27 13:41:36.765152

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a9af853b438f'
down_revision = '67f5508094e3'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column('posts', sa.Column('content', sa.String(), nullable=False))


def downgrade() -> None:
    op.drop_column('posts', 'content')
