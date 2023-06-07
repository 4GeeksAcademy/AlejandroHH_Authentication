"""empty message

Revision ID: 878175fd5afc
Revises: 2a3d1dd939b5
Create Date: 2023-06-05 15:24:45.244290

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '878175fd5afc'
down_revision = '2a3d1dd939b5'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.add_column(sa.Column('name', sa.String(length=80), nullable=False))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.drop_column('name')

    # ### end Alembic commands ###