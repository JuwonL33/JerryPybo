"""empty message

Revision ID: 53ae70153377
Revises: d45a6cc31e95
Create Date: 2022-03-28 21:41:05.011192

"""
from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = '53ae70153377'
down_revision = 'd45a6cc31e95'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('answer', schema=None) as batch_op:
        batch_op.alter_column('user_id',
                              existing_type=sa.INTEGER(),
                              nullable=False,
                              existing_server_default=sa.text("'1'"))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('answer', schema=None) as batch_op:
        batch_op.alter_column('user_id',
                              existing_type=sa.INTEGER(),
                              nullable=True,
                              existing_server_default=sa.text("'1'"))

    # ### end Alembic commands ###
