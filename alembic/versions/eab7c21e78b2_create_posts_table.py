"""create posts table

Revision ID: eab7c21e78b2
Revises: 
Create Date: 2022-07-11 17:41:26.825436

"""
from alembic import op
import sqlalchemy


# revision identifiers, used by Alembic.
revision = 'eab7c21e78b2'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('posts',sqlalchemy.Column('id',sqlalchemy.Integer,nullable=False,primary_key=True),
    sqlalchemy.Column('title',sqlalchemy.String(),nullable=False))
    pass


def downgrade():
    op.drop_table('posts')
    pass
