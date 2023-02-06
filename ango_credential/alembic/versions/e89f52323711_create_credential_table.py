"""create_credential_table

Revision ID: e89f52323711
Revises:
Create Date: 2023-02-06 11:31:32.776929

"""
import uuid

import sqlalchemy as sa
from alembic import op
from sqlalchemy.dialects.postgresql import UUID

# revision identifiers, used by Alembic.
revision = "e89f52323711"
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        "credential",
        sa.Column("id", UUID(as_uuid=True), primary_key=True, default=uuid.uuid4),
        sa.Column("user_id", UUID(as_uuid=True)),
        sa.Column("domain", sa.String(255)),
        sa.Column("name", sa.String(255), nullable=False),
        sa.Column("username", sa.String(255)),
        sa.Column("pass_encrypted", sa.LargeBinary, nullable=False),
        sa.Column("created_at", sa.types.TIMESTAMP, nullable=False),
        sa.Column("updated_at", sa.types.TIMESTAMP),
    )


def downgrade() -> None:
    op.drop_table("credential")
