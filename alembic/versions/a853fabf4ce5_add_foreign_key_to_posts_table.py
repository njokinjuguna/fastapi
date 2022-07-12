"""add foreign-key to posts table

Revision ID: a853fabf4ce5
Revises: 934592225f42
Create Date: 2022-07-12 12:54:45.124815

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a853fabf4ce5'
down_revision = '934592225f42'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('posts',sa.Column('owner_id',sa.Integer(),nullable=False))
    op.create_foreign_key('post_users_fk',source_table='posts',referent_table="users",
    local_cols=['owner_id'],remote_cols=['id'],ondelete='CASCADE'
    )
    pass


def downgrade():
    op.drop_constraint('post_users_fk',table_name="posts")
    op.drop_column('posts','owner_id')
    pass
