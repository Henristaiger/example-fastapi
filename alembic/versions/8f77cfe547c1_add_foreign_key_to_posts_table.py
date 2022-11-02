"""add foreign-key to posts table

Revision ID: 8f77cfe547c1
Revises: de7c02a7b0fe
Create Date: 2022-11-02 11:36:03.861505

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '8f77cfe547c1'
down_revision = 'de7c02a7b0fe'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column("posts", sa.Column("owner_id", sa.Integer(), nullable=False))
    op.create_foreign_key("posts_users_fk", source_table="posts", referent_table="users",
                            local_cols=["owner_id"], remote_cols=["id"], ondelete="CASCADE")


def downgrade() -> None:
    op.drop_constraint("posts_users_fk", table_name="posts")
    op.drop_column("posts", "owner_id")
