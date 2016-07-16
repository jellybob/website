"""

Revision ID: 2ad5fa906742
Revises: e303484d5984
Create Date: 2016-07-15 16:28:34.551708

"""

# revision identifiers, used by Alembic.
revision = '2ad5fa906742'
down_revision = 'e303484d5984'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.create_table('venue',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.Column('type', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id', name=op.f('pk_venue'))
    )
    with op.batch_alter_table(u'proposal', schema=None) as batch_op:
        batch_op.add_column(sa.Column('allowed_times', sa.String(), nullable=True))
        batch_op.add_column(sa.Column('allowed_venues', sa.String(), nullable=True))
        batch_op.add_column(sa.Column('scheduled_duration', sa.Integer(), nullable=True))
        batch_op.add_column(sa.Column('scheduled_time', sa.DateTime(), nullable=True))
        batch_op.add_column(sa.Column('scheduled_venue', sa.Integer(), nullable=True))
        batch_op.create_foreign_key(batch_op.f('fk_proposal_scheduled_venue_venue'), 'venue', ['scheduled_venue'], ['id'])

    with op.batch_alter_table(u'proposal_version', schema=None) as batch_op:
        batch_op.add_column(sa.Column('allowed_times', sa.String(), autoincrement=False, nullable=True))
        batch_op.add_column(sa.Column('allowed_venues', sa.String(), autoincrement=False, nullable=True))
        batch_op.add_column(sa.Column('scheduled_duration', sa.Integer(), autoincrement=False, nullable=True))
        batch_op.add_column(sa.Column('scheduled_time', sa.DateTime(), autoincrement=False, nullable=True))
        batch_op.add_column(sa.Column('scheduled_venue', sa.Integer(), autoincrement=False, nullable=True))

    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table(u'proposal_version', schema=None) as batch_op:
        batch_op.drop_column('scheduled_venue')
        batch_op.drop_column('scheduled_time')
        batch_op.drop_column('scheduled_duration')
        batch_op.drop_column('allowed_venues')
        batch_op.drop_column('allowed_times')

    with op.batch_alter_table(u'proposal', schema=None) as batch_op:
        batch_op.drop_constraint(batch_op.f('fk_proposal_scheduled_venue_venue'), type_='foreignkey')
        batch_op.drop_column('scheduled_venue')
        batch_op.drop_column('scheduled_time')
        batch_op.drop_column('scheduled_duration')
        batch_op.drop_column('allowed_venues')
        batch_op.drop_column('allowed_times')

    op.drop_table('venue')
    ### end Alembic commands ###