from typing import List
from uuid import UUID

import ango_credential.app.dao.credential as credential_dao
from ango_credential.app.core.exceptions import AuthException
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
    new_credential = CredentialCreate(**create_request.dict())
    created_credential = credential_dao.create(new_credential)
    return created_credential


def get_credential_by_user_id(user_id: UUID) -> List[CredentialDb] | None:
    return credential_dao.get_credential_by_user_id(user_id=user_id)


def get_credential_by_domain_name(domain_name: str) -> CredentialDb | None:
    return credential_dao.get_credential_by_domain_name(domain_name=domain_name)


def update(update_request: CredentialUpdateRequest):
    return credential_dao.update(update_request)


def delete(delete_request: CredentialDeleteRequest):
    credential_dao.delete(delete_request)
