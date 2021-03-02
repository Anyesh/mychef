"""initial commit

Revision ID: c8137c750b21
Create Date: 2020-10-09 08:33:48.296041

"""
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

from alembic import op

# revision identifiers, used by Alembic.
revision = "c8137c750b21"
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "sources",
        sa.Column("id", sa.INTEGER(), autoincrement=True, nullable=False),
        sa.Column("name", sa.VARCHAR(length=255), autoincrement=False, nullable=False),
        sa.Column("url", sa.VARCHAR(length=255), autoincrement=False, nullable=False),
        sa.Column("ts", postgresql.TIMESTAMP(), autoincrement=False, nullable=False),
        sa.PrimaryKeyConstraint("id", name="sources_pkey"),
        sa.UniqueConstraint("url", name="sources_url_key"),
    )
    op.create_table(
        "ingredients",
        sa.Column("id", sa.INTEGER(), autoincrement=True, nullable=False),
        sa.Column(
            "ingredient", sa.VARCHAR(length=255), autoincrement=False, nullable=False
        ),
        sa.Column("ts", postgresql.TIMESTAMP(), autoincrement=False, nullable=False),
        sa.PrimaryKeyConstraint("id", name="ingredients_pkey"),
        sa.UniqueConstraint("ingredient", name="ingredients_ingredient_key"),
    )
    op.create_table(
        "recipes",
        sa.Column("id", sa.INTEGER(), autoincrement=True, nullable=False),
        sa.Column("source", sa.INTEGER(), autoincrement=False, nullable=False),
        sa.Column("name", sa.VARCHAR(length=255), autoincrement=False, nullable=False),
        sa.Column("url", sa.VARCHAR(length=255), autoincrement=False, nullable=False),
        sa.Column("image", sa.VARCHAR(length=255), autoincrement=False, nullable=False),
        sa.Column(
            "ingredients",
            postgresql.JSON(astext_type=sa.Text()),
            autoincrement=False,
            nullable=False,
        ),
        sa.Column("ts", postgresql.TIMESTAMP(), autoincrement=False, nullable=False),
        sa.ForeignKeyConstraint(["source"], ["sources.id"], name="recipes_source_fkey"),
        sa.PrimaryKeyConstraint("id", name="recipes_pkey"),
        sa.UniqueConstraint("url", name="recipes_url_key"),
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table("ingredients")
    op.drop_table("sources")
    op.drop_table("recipes")
    # ### end Alembic commands ###
