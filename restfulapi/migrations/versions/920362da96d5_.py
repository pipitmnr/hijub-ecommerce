"""empty message

Revision ID: 920362da96d5
Revises: af2614a3ce9c
Create Date: 2020-01-05 10:51:25.512286

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '920362da96d5'
down_revision = 'af2614a3ce9c'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index('alamat_lengkap', table_name='cart')
    op.drop_index('keterangan', table_name='product')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_index('keterangan', 'product', ['keterangan'], unique=True)
    op.create_index('alamat_lengkap', 'cart', ['alamat_lengkap'], unique=True)
    # ### end Alembic commands ###
