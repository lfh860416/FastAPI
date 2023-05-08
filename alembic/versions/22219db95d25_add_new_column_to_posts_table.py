"""add new column to posts table

Revision ID: 22219db95d25
Revises: 4901e90f1dcb
Create Date: 2023-04-26 12:36:40.404170

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '22219db95d25'
down_revision = '4901e90f1dcb'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column('posts', sa.Column('content', sa.String(), nullable=False))
    pass


def downgrade() -> None:
    op.drop_column('posts', 'content')
    pass
