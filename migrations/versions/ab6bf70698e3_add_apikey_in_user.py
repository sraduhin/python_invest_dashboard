"""add APIKEY in user

Revision ID: ab6bf70698e3
Revises: 5662b3812a74
Create Date: 2022-07-13 12:50:34.183137

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ab6bf70698e3'
down_revision = '5662b3812a74'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('API_KEY', sa.String(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('user', 'API_KEY')
    # ### end Alembic commands ###