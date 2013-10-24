"""empty message

Revision ID: 85d9c0b5114
Revises: None
Create Date: 2013-10-25 11:26:38.501853

"""

# revision identifiers, used by Alembic.
revision = '85d9c0b5114'
down_revision = None

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.create_table('beer',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=80), nullable=True),
    sa.Column('style', sa.String(length=80), nullable=True),
    sa.Column('description', sa.String(length=250), nullable=True),
    sa.Column('abv', sa.Float(), nullable=True),
    sa.Column('ibu', sa.Integer(), nullable=True),
    sa.Column('volume', sa.Float(), nullable=True),
    sa.Column('date_brewed', sa.Date(), nullable=True),
    sa.Column('date_tapped', sa.Date(), nullable=True),
    sa.Column('date_retired', sa.Date(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('tap',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('position', sa.Integer(), nullable=True),
    sa.Column('name', sa.String(length=80), nullable=True),
    sa.Column('beer_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['beer_id'], ['beer.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('position')
    )
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('tap')
    op.drop_table('beer')
    ### end Alembic commands ###
