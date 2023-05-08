"""create posts table

Revision ID: 4901e90f1dcb
Revises: 
Create Date: 2023-04-26 10:27:28.718207

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '4901e90f1dcb'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table('posts', sa.Column('id', sa.Integer(), nullable=False,
                    primary_key=True), sa.Column('title', sa.String(), nullable=False))
    pass


def downgrade() -> None:
    op.drop_table('posts')
    pass
