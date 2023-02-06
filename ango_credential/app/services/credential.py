from datetime import datetime
from typing import List
from uuid import UUID

import ango_credential.app.dao.credential as credential_dao
from ango_credential.app.core.exceptions import AuthException, BadRequestException
from ango_credential.app.models.credential import (
    Credential,
    CredentialCreate,
    CredentialCreateRequest,
    CredentialDb,
    CredentialDeleteRequest,
    CredentialUpdateRequest,
)
from ango_credential.app.schemas.credential import Credential as CredentialOrm


def create(create_request: CredentialCreateRequest) -> CredentialDb:
    if not create_request.name and not create_request.domain:
        raise BadRequestException(message="Both name and domain cannot be empty")

    if not create_request.name:
        create_request.name = create_request.domain

    new_credential = CredentialCreate(**create_request.dict(), created_at=datetime.now())
    created_credential = credential_dao.create(new_credential)
    return created_credential


def get_credential_by_user_id(user_id: UUID) -> List[CredentialDb] | None:
    return credential_dao.get_credential_by_user_id(user_id=user_id)


def get_credential_by_domain(domain: str, user_id: UUID) -> list[CredentialDb]:
    return credential_dao.get_credential_by_domain(domain, user_id)


def update(update_request: CredentialUpdateRequest):
    return credential_dao.update(update_request)


def delete(delete_request: CredentialDeleteRequest):
    credential_dao.delete(delete_request)
