from typing import List, Optional
from uuid import UUID

from fastapi import APIRouter, Depends

import ango_credential.app.services.credential as credential_service
from ango_credential.app.core.config import Settings
from ango_credential.app.core.exceptions import AuthException
from ango_credential.app.middleware.auth import check_auth
from ango_credential.app.models.auth import TokenData
from ango_credential.app.models.credential import (
    Credential,
    CredentialCreateRequest,
    CredentialDb,
    CredentialDeleteRequest,
    CredentialUpdateRequest,
)

credential_router = APIRouter()
settings = Settings()


@credential_router.get("/user/{user_id}", dependencies=[Depends(check_auth)])
def get_credentials(user_id: UUID) -> List[CredentialDb] | None:
    credentials = credential_service.get_credential_by_user_id(user_id=user_id)
    return credentials


@credential_router.post("/", dependencies=[Depends(check_auth)])
def create_credential(create_request: CredentialCreateRequest) -> CredentialDb:
    credential = credential_service.create(create_request)
    return credential


@credential_router.get("/", dependencies=[Depends(check_auth)])
def get_credential_by_domain(domain: str, user_id: UUID) -> list[CredentialDb]:
    credential = credential_service.get_credential_by_domain(domain, user_id)
    return credential


@credential_router.put("/", dependencies=[Depends(check_auth)])
def update_credential(request: CredentialUpdateRequest):
    credential_service.update(request)
    return "Credential updated"


@credential_router.delete("/", dependencies=[Depends(check_auth)])
def delete_credential(request: CredentialDeleteRequest):
    credential_service.delete(request)
    return "Credential deleted"
