"""Changed resource_id

Revision ID: 2f658fe6e93
Revises: 236ad45a9e4
Create Date: 2015-07-28 11:26:16.508610

"""

# revision identifiers, used by Alembic.
revision = '2f658fe6e93'
down_revision = '236ad45a9e4'
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
    op.alter_column('service_usage', 'resource_id',
               existing_type=mysql.TEXT(),
               type_=sa.String(length=100),
               existing_nullable=True)
    ### end Alembic commands ###


def downgrade_account():
    ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('service_usage', 'resource_id',
               existing_type=sa.String(length=100),
               type_=mysql.TEXT(),
               existing_nullable=True)
    ### end Alembic commands ###


def upgrade_fitter():
    pass


def downgrade_fitter():
    pass

