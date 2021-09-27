"""empty message

Revision ID: 768f86fd13e7
Revises: 580067b49971
Create Date: 2021-09-26 21:38:41.111901

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '768f86fd13e7'
down_revision = '580067b49971'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('adresses', sa.Column('user_idasdasdasdsa', sa.Integer(), nullable=True))
    op.drop_constraint(None, 'adresses', type_='foreignkey')
    op.create_foreign_key(None, 'adresses', 'users', ['user_idasdasdasdsa'], ['id'])
    op.drop_column('adresses', 'user_id')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('adresses', sa.Column('user_id', sa.INTEGER(), nullable=True))
    op.drop_constraint(None, 'adresses', type_='foreignkey')
    op.create_foreign_key(None, 'adresses', 'users', ['user_id'], ['id'])
    op.drop_column('adresses', 'user_idasdasdasdsa')
    # ### end Alembic commands ###