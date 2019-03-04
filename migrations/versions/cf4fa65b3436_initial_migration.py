"""Initial Migration

Revision ID: cf4fa65b3436
Revises: 52ef7ff22ff0
Create Date: 2019-03-04 09:04:39.537684

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'cf4fa65b3436'
down_revision = '52ef7ff22ff0'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint('comments_user_id_fkey', 'comments', type_='foreignkey')
    op.drop_column('comments', 'user_id')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('comments', sa.Column('user_id', sa.INTEGER(), autoincrement=False, nullable=True))
    op.create_foreign_key('comments_user_id_fkey', 'comments', 'users', ['user_id'], ['id'])
    # ### end Alembic commands ###