"""empty message

Revision ID: aa266f59b8b9
Revises: 
Create Date: 2021-10-02 16:00:02.745191

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'aa266f59b8b9'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('marvel',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('character_name', sa.String(length=100), nullable=False),
    sa.Column('super_power', sa.String(length=100), nullable=True),
    sa.Column('comics_appeared_in', sa.String(length=300), nullable=True),
    sa.Column('hero_or_villain', sa.String(length=100), nullable=True),
    sa.Column('description', sa.String(length=400), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('character_name')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('marvel')
    # ### end Alembic commands ###
