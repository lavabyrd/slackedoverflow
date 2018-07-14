"""init

Revision ID: ba841675a548
Revises: 
Create Date: 2018-07-14 10:23:44.387554

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ba841675a548'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('post',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('message_text', sa.String(length=256), nullable=True),
    sa.Column('date_added', sa.DateTime(), nullable=True),
    sa.Column('team_id', sa.String(length=16), nullable=True),
    sa.Column('team_domain', sa.String(length=64), nullable=True),
    sa.Column('user_added', sa.String(length=16), nullable=True),
    sa.Column('user_posted', sa.String(length=16), nullable=True),
    sa.Column('ts_posted', sa.String(length=16), nullable=True),
    sa.Column('channel', sa.String(length=16), nullable=True),
    sa.Column('replies', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_post_channel'), 'post', ['channel'], unique=False)
    op.create_index(op.f('ix_post_date_added'), 'post', ['date_added'], unique=False)
    op.create_index(op.f('ix_post_replies'), 'post', ['replies'], unique=False)
    op.create_index(op.f('ix_post_team_domain'), 'post', ['team_domain'], unique=False)
    op.create_index(op.f('ix_post_team_id'), 'post', ['team_id'], unique=False)
    op.create_index(op.f('ix_post_user_added'), 'post', ['user_added'], unique=False)
    op.create_index(op.f('ix_post_user_posted'), 'post', ['user_posted'], unique=False)
    op.create_table('token',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('team_id', sa.String(length=30), nullable=True),
    sa.Column('user_id', sa.String(length=30), nullable=True),
    sa.Column('timestamp', sa.DateTime(), nullable=True),
    sa.Column('token', sa.String(length=120), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_token_timestamp'), 'token', ['timestamp'], unique=False)
    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(length=64), nullable=True),
    sa.Column('email', sa.String(length=120), nullable=True),
    sa.Column('password_hash', sa.String(length=128), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_user_email'), 'user', ['email'], unique=True)
    op.create_index(op.f('ix_user_username'), 'user', ['username'], unique=True)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_user_username'), table_name='user')
    op.drop_index(op.f('ix_user_email'), table_name='user')
    op.drop_table('user')
    op.drop_index(op.f('ix_token_timestamp'), table_name='token')
    op.drop_table('token')
    op.drop_index(op.f('ix_post_user_posted'), table_name='post')
    op.drop_index(op.f('ix_post_user_added'), table_name='post')
    op.drop_index(op.f('ix_post_team_id'), table_name='post')
    op.drop_index(op.f('ix_post_team_domain'), table_name='post')
    op.drop_index(op.f('ix_post_replies'), table_name='post')
    op.drop_index(op.f('ix_post_date_added'), table_name='post')
    op.drop_index(op.f('ix_post_channel'), table_name='post')
    op.drop_table('post')
    # ### end Alembic commands ###
