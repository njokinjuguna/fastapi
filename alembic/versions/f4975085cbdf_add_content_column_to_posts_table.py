"""add content column to posts table

Revision ID: f4975085cbdf
Revises: eab7c21e78b2
Create Date: 2022-07-12 10:55:40.601344

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f4975085cbdf'
down_revision = 'eab7c21e78b2'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('posts',sa.Column('content',sa.String(),nullable=False))
    pass


def downgrade():
    op.drop_column('posts','content')
    pass
