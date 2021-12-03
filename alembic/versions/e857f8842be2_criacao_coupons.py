"""criacao coupons

Revision ID: e857f8842be2
Revises: 98fc4f7d77d9
Create Date: 2021-12-03 17:35:58.320513

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e857f8842be2'
down_revision = '98fc4f7d77d9'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('coupons',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('code', sa.String(length=10), nullable=True),
    sa.Column('expire_at', sa.DATETIME(), nullable=True),
    sa.Column('limit', sa.Integer(), nullable=True),
    sa.Column('type', sa.String(length=15), nullable=True),
    sa.Column('value', sa.Float(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('coupons')
    # ### end Alembic commands ###
