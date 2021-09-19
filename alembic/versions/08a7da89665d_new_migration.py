"""New Migration

Revision ID: 08a7da89665d
Revises: 12166bb218a7
Create Date: 2021-09-19 22:37:45.450858

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '08a7da89665d'
down_revision = '12166bb218a7'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('book', sa.Column('author_id', sa.Integer(), nullable=True))
    op.drop_constraint('book_auhtor_id_fkey', 'book', type_='foreignkey')
    op.create_foreign_key(None, 'book', 'author', ['author_id'], ['id'])
    op.drop_column('book', 'auhtor_id')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('book', sa.Column('auhtor_id', sa.INTEGER(), autoincrement=False, nullable=True))
    op.drop_constraint(None, 'book', type_='foreignkey')
    op.create_foreign_key('book_auhtor_id_fkey', 'book', 'author', ['auhtor_id'], ['id'])
    op.drop_column('book', 'author_id')
    # ### end Alembic commands ###