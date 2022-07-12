"""add publish & created_at columns to posts table

Revision ID: 441bd043fbcb
Revises: a853fabf4ce5
Create Date: 2022-07-12 15:13:35.484151

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '441bd043fbcb'
down_revision = 'a853fabf4ce5'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('posts',sa.Column('published', sa.Boolean(), nullable=False, server_default='TRUE'),)
    op.add_column('posts',sa.Column('created_at', sa.TIMESTAMP(timezone=True), nullable=False, server_default=sa.text('NOW()')),)


    pass


def downgrade():
    op.drop_column('posts','published')
    op.drop_column('posts','created_at')
    pass


