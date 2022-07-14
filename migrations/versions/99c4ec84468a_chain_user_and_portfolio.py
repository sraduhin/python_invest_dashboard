"""chain User and Portfolio

Revision ID: 99c4ec84468a
Revises: 62e21b8f3527
Create Date: 2022-07-13 15:23:14.813284

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '99c4ec84468a'
down_revision = '62e21b8f3527'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('portfolio', sa.Column('user_id', sa.Integer(), nullable=False))
    op.add_column('user', sa.Column('api_key', sa.String(length=128), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('user', 'api_key')
    op.drop_column('portfolio', 'user_id')
    # ### end Alembic commands ###