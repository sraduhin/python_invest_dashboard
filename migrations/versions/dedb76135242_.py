"""empty message

Revision ID: dedb76135242
Revises: b0459d7f5f4d
Create Date: 2022-07-13 15:48:35.319976

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'dedb76135242'
down_revision = 'b0459d7f5f4d'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('instrument',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('figi', sa.String(), nullable=True),
    sa.Column('tiker', sa.String(), nullable=True),
    sa.Column('type', sa.String(), nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.Column('currency', sa.String(), nullable=False),
    sa.Column('sector', sa.String(length=30), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('news',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(), nullable=False),
    sa.Column('url', sa.String(), nullable=False),
    sa.Column('published', sa.DateTime(), nullable=False),
    sa.Column('text', sa.Text(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('url')
    )
    op.create_table('portfolio',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('account_id', sa.String(), nullable=True),
    sa.Column('expected_yield', sa.Float(), nullable=True),
    sa.Column('total_shares', sa.Float(), nullable=True),
    sa.Column('total_bonds', sa.Float(), nullable=True),
    sa.Column('total_etf', sa.Float(), nullable=True),
    sa.Column('total_currencies', sa.Float(), nullable=True),
    sa.Column('total_futures', sa.Float(), nullable=True),
    sa.Column('type', sa.String(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=64), nullable=True),
    sa.Column('username', sa.String(length=32), nullable=True),
    sa.Column('password', sa.String(length=128), nullable=True),
    sa.Column('api_key', sa.String(length=128), nullable=True),
    sa.Column('role', sa.String(length=10), nullable=True),
    sa.Column('email', sa.String(length=50), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_user_role'), 'user', ['role'], unique=False)
    op.create_index(op.f('ix_user_username'), 'user', ['username'], unique=True)
    op.create_table('position',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('portfolio_id', sa.Integer(), nullable=False),
    sa.Column('instrument_id', sa.String(), nullable=False),
    sa.Column('figi', sa.String(), nullable=True),
    sa.Column('amount', sa.Float(), nullable=False),
    sa.Column('expected_yield', sa.Float(), nullable=False),
    sa.Column('average_price', sa.Float(), nullable=False),
    sa.Column('current_price', sa.Float(), nullable=False),
    sa.ForeignKeyConstraint(['instrument_id'], ['instrument.id'], ),
    sa.ForeignKeyConstraint(['portfolio_id'], ['portfolio.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_position_instrument_id'), 'position', ['instrument_id'], unique=False)
    op.create_index(op.f('ix_position_portfolio_id'), 'position', ['portfolio_id'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_position_portfolio_id'), table_name='position')
    op.drop_index(op.f('ix_position_instrument_id'), table_name='position')
    op.drop_table('position')
    op.drop_index(op.f('ix_user_username'), table_name='user')
    op.drop_index(op.f('ix_user_role'), table_name='user')
    op.drop_table('user')
    op.drop_table('portfolio')
    op.drop_table('news')
    op.drop_table('instrument')
    # ### end Alembic commands ###
