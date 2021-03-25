"""Updated schema, changed username to name

Revision ID: 63188ee61c3d
Revises: ee9381258dc6
Create Date: 2021-03-17 20:13:42.906780

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '63188ee61c3d'
down_revision = 'ee9381258dc6'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('chat', sa.Column('name', sa.String(length=64), nullable=True))
    op.drop_column('chat', 'username')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('chat', sa.Column('username', sa.VARCHAR(length=64), nullable=True))
    op.drop_column('chat', 'name')
    # ### end Alembic commands ###