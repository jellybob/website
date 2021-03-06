"""Add tickets_remaining to voucher

Revision ID: 74348e4e2246
Revises: 972ff3647ce2
Create Date: 2020-01-03 18:44:43.177283

"""

# revision identifiers, used by Alembic.
revision = '74348e4e2246'
down_revision = '972ff3647ce2'

from alembic import op
import sqlalchemy as sa


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('voucher', sa.Column('tickets_remaining', sa.Integer(), server_default='2', nullable=False))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('voucher', 'tickets_remaining')
    # ### end Alembic commands ###
