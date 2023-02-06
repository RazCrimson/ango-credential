from uuid import uuid4

from sqlalchemy import TIMESTAMP, Column, LargeBinary, String
from sqlalchemy.dialects.postgresql import UUID

from ango_credential.app.db.base_class import Base


class Credential(Base):
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid4)
    user_id = Column(UUID(as_uuid=True))
    name = Column(String)
    domain_name = Column(String)
    pass_encrypted = Column(LargeBinary)
    created_at = Column(TIMESTAMP)
    updated_at = Column(TIMESTAMP)

    def __repr__(self):
        return f"<Credential(id={self.id}, user_id={self.user_id}, name={self.name}, domain_name={self.domain_name}, update_at={self.updated_at})>"
