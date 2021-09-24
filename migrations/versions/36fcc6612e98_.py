"""empty message

Revision ID: 36fcc6612e98
Revises: 55ad7aa5637b
Create Date: 2021-09-24 17:11:37.743920

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '36fcc6612e98'
down_revision = '55ad7aa5637b'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('users', 'money',
               existing_type=sa.INTEGER(),
               type_=sa.Float(),
               existing_nullable=False)
    op.alter_column('users', 'gender',
               existing_type=sa.VARCHAR(length=20),
               nullable=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('users', 'gender',
               existing_type=sa.VARCHAR(length=20),
               nullable=True)
    op.alter_column('users', 'money',
               existing_type=sa.Float(),
               type_=sa.INTEGER(),
               existing_nullable=False)
    # ### end Alembic commands ###