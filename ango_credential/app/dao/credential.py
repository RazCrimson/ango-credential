from typing import List
from uuid import UUID

import sqlalchemy.exc

from ango_credential.app.core.config import Settings
from ango_credential.app.core.exceptions import DuplicateRecordException
from ango_credential.app.db.connection import DbConnector
from ango_credential.app.models.credential import (
    CredentialCreate,
    CredentialDb,
    CredentialDeleteRequest,
    CredentialUpdateRequest,
)
from ango_credential.app.schemas.credential import Credential as CredentialOrm

settings = Settings()

db_connector = DbConnector(settings.DATABASE_URI)


def create(credential_data: CredentialCreate) -> CredentialDb:
    session = db_connector.get_session()
    new_credential_db = CredentialOrm(**credential_data.dict())

    try:
        session.add(new_credential_db)
        session.commit()
    except sqlalchemy.exc.IntegrityError:
        raise DuplicateRecordException(message="Credential already exists.")

    return CredentialDb.from_orm(new_credential_db)


def get_credential_by_user_id(user_id: UUID) -> List[CredentialDb] | None:
    session = db_connector.get_session()
    credentials = list(session.query(CredentialOrm).filter(CredentialOrm.user_id == user_id))
    return [CredentialDb.from_orm(credential) for credential in credentials] if credentials else None


def get_credential_by_domain(domain: str, user_id: UUID) -> list[CredentialDb]:
    session = db_connector.get_session()
    credentials = list(
        session.query(CredentialOrm).filter(CredentialOrm.domain == domain and CredentialOrm.user_id == user_id)
    )
    return [CredentialDb.from_orm(credential) for credential in credentials] if credentials else []


def update(credential_data: CredentialUpdateRequest):
    session = db_connector.get_session()
    session.query(CredentialOrm).filter(CredentialOrm.id == credential_data.id).update(credential_data.dict())
    session.commit()


def delete(credential: CredentialDeleteRequest):
    session = db_connector.get_session()
    session.query(CredentialOrm).filter(CredentialOrm.id == credential.id).delete()
    session.commit()
