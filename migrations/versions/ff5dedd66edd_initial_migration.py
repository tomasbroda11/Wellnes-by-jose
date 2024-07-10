"""initial migration

Revision ID: ff5dedd66edd
Revises: 
Create Date: 2024-07-09 17:45:23.316316

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ff5dedd66edd'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('contact', schema=None) as batch_op:
        batch_op.add_column(sa.Column('telefono', sa.String(length=15), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('contact', schema=None) as batch_op:
        batch_op.drop_column('telefono')

    # ### end Alembic commands ###
