"""create table profile

Revision ID: 0e2b1cc8ba46
Revises: 11b65f95fee7
Create Date: 2024-05-15 20:08:00.707088

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "0e2b1cc8ba46"
down_revision: Union[str, None] = "11b65f95fee7"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "profiles",
        sa.Column("first_name", sa.String(length=30), nullable=True),
        sa.Column("last_name", sa.String(length=30), nullable=True),
        sa.Column("bio", sa.String(), nullable=True),
        sa.Column("user_id", sa.Integer(), nullable=False),
        sa.Column("id", sa.Integer(), nullable=False),
        sa.ForeignKeyConstraint(
            ["user_id"],
            ["users.id"],
        ),
        sa.PrimaryKeyConstraint("id"),
        sa.UniqueConstraint("user_id"),
    )
    op.add_column(
        "posts", sa.Column("body", sa.Text(), server_default="", nullable=False)
    )
    op.drop_column("posts", "content")
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column(
        "posts",
        sa.Column(
            "content",
            sa.TEXT(),
            server_default=sa.text("''::text"),
            autoincrement=False,
            nullable=False,
        ),
    )
    op.drop_column("posts", "body")
    op.drop_table("profiles")
    # ### end Alembic commands ###
