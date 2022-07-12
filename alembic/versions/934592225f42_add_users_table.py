"""add users table

Revision ID: 934592225f42
Revises: f4975085cbdf
Create Date: 2022-07-12 12:15:55.025577

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '934592225f42'
down_revision = 'f4975085cbdf'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('users',

        sa.Column('id',sa.Integer(),nullable=False),
        sa.Column('email',sa.String(),nullable=False),
        sa.Column('password',sa.String(),nullable=False),
        sa.Column('created_at',sa.TIMESTAMP(timezone=True),
        server_default=sa.text('now()'),nullable=False),
        sa.PrimaryKeyConstraint('id'),
        sa.UniqueConstraint('email')
        )
    pass


def downgrade():
    op.drop_table('users')
    pass
