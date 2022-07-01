"""users and news tables

Revision ID: 02bce31e66da
Revises: 
Create Date: 2022-07-01 10:21:55.394631

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '02bce31e66da'
down_revision = None
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
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('portfolio',
    sa.Column('id', sa.Integer(), nullable=False),
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
    sa.Column('username', sa.String(length=64), nullable=True),
    sa.Column('password', sa.String(length=128), nullable=True),
    sa.Column('role', sa.String(length=10), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_user_role'), 'user', ['role'], unique=False)
    op.create_index(op.f('ix_user_username'), 'user', ['username'], unique=True)
    op.create_table('position',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('portfolio_id', sa.Integer(), nullable=False),
    sa.Column('instrument_id', sa.String(), nullable=False),
    sa.Column('amount', sa.Float(), nullable=False),
    sa.Column('expected_yield', sa.Float(), nullable=False),
    sa.Column('average_price', sa.Float(), nullable=False),
    sa.Column('current_price', sa.Float(), nullable=False),
    sa.Column('lots', sa.Float(), nullable=False),
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
    op.drop_table('instrument')
    # ### end Alembic commands ###
