"""empty message

Revision ID: 9d48bdb4e70e
Revises: 7164272dc0d3
Create Date: 2023-01-27 13:35:24.625381

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9d48bdb4e70e'
down_revision = '7164272dc0d3'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('vehicles', schema=None) as batch_op:
        batch_op.add_column(sa.Column('model', sa.String(length=120), nullable=False))
        batch_op.create_unique_constraint(None, ['model'])

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('vehicles', schema=None) as batch_op:
        batch_op.drop_constraint(None, type_='unique')
        batch_op.drop_column('model')

    # ### end Alembic commands ###