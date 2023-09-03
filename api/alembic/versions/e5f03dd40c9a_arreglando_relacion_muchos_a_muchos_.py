"""arreglando relacion muchos-a-muchos entre docentes y grados

Revision ID: e5f03dd40c9a
Revises: c659b39a6fa8
Create Date: 2023-09-03 08:16:13.384826

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'e5f03dd40c9a'
down_revision: Union[str, None] = 'c659b39a6fa8'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('grados_docentes',
    sa.Column('grado_id', sa.Integer(), nullable=True),
    sa.Column('docente_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['docente_id'], ['Docentes.ID'], ),
    sa.ForeignKeyConstraint(['grado_id'], ['Grados.ID'], )
    )
    op.add_column('Usuarios', sa.Column('Activo', sa.Boolean(), nullable=True))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('Usuarios', 'Activo')
    op.drop_table('grados_docentes')
    # ### end Alembic commands ###
