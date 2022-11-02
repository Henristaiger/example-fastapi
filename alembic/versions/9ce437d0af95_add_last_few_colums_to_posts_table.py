"""add last few colums to posts table

Revision ID: 9ce437d0af95
Revises: 8f77cfe547c1
Create Date: 2022-11-02 13:17:04.149799

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9ce437d0af95'
down_revision = '8f77cfe547c1'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column("posts", sa.Column(
        "published", sa.Boolean(), nullable=False, server_default="TRUE"))
    op.add_column("posts", sa.Column(
        "created_at", sa.TIMESTAMP(timezone=True), nullable=False, server_default=sa.text("NOW()")))


def downgrade() -> None:
    op.drop_column("posts", "published")
    op.drop_column("posts", "created_at")
