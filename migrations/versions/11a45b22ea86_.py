"""empty message

Revision ID: 11a45b22ea86
Revises: 
Create Date: 2023-07-27 17:59:01.273150

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '11a45b22ea86'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('builds',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('componentlist_id', sa.Integer(), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['componentlist_id'], ['componentlists.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('componentlists',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('component_id', sa.Integer(), nullable=True),
    sa.Column('build_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['build_id'], ['builds.id'], ),
    sa.ForeignKeyConstraint(['component_id'], ['components.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('components',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=64), nullable=True),
    sa.Column('description', sa.String(), nullable=True),
    sa.Column('image_link', sa.String(length=128), nullable=True),
    sa.Column('type', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('users',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('first_name', sa.String(length=64), nullable=True),
    sa.Column('last_name', sa.String(length=64), nullable=True),
    sa.Column('email', sa.String(length=64), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('users')
    op.drop_table('components')
    op.drop_table('componentlists')
    op.drop_table('builds')
    # ### end Alembic commands ###
