"""Added last_seen attribute

Revision ID: 129572aca3ae
Revises: 
Create Date: 2024-03-29 16:45:16.020494

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '129572aca3ae'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.add_column(sa.Column('last_seen', sa.DateTime(), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.drop_column('last_seen')

    # ### end Alembic commands ###
