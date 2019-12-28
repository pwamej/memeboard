"""empty message

Revision ID: 650ed3ffd8f0
Revises: 
Create Date: 2019-12-25 17:41:11.058979

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '650ed3ffd8f0'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user',
    sa.Column('id', sa.String(length=64), nullable=False),
    sa.Column('email', sa.String(length=128), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email')
    )
    op.create_table('user_role',
    sa.Column('user_id', sa.String(length=64), nullable=False),
    sa.Column('role', sa.String(length=64), nullable=False),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('user_id', 'role')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('user_role')
    op.drop_table('user')
    # ### end Alembic commands ###
