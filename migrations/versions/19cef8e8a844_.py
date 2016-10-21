"""empty message

Revision ID: 19cef8e8a844
Revises: 4eecec0405d0
Create Date: 2016-10-21 10:02:15.975297

"""

# revision identifiers, used by Alembic.
revision = '19cef8e8a844'
down_revision = '4eecec0405d0'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.create_table('votes',
    sa.Column('post_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['post_id'], ['posts.id'], ),
    sa.PrimaryKeyConstraint('post_id')
    )
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('votes')
    ### end Alembic commands ###
