"""Increase size of name field

Revision ID: 37b9ec06ce4
Revises: 5ef06a3e19
Create Date: 2015-06-24 13:27:14.756793

"""

# revision identifiers, used by Alembic.
revision = '37b9ec06ce4'
down_revision = '5ef06a3e19'
branch_labels = None
depends_on = None

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

def upgrade(engine_name):
    globals()["upgrade_%s" % engine_name]()


def downgrade(engine_name):
    globals()["downgrade_%s" % engine_name]()





def upgrade_account():
    ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('user', 'name',
               existing_type=mysql.VARCHAR(length=64),
               type_=sa.String(length=256),
               existing_nullable=True)
    ### end Alembic commands ###


def downgrade_account():
    ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('user', 'name',
               existing_type=sa.String(length=256),
               type_=mysql.VARCHAR(length=64),
               existing_nullable=True)
    ### end Alembic commands ###


def upgrade_fitter():
    pass


def downgrade_fitter():
    pass
