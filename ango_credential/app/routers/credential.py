from typing import List

from fastapi import APIRouter, Depends

import ango_credential.app.services.credential as credential_service
from ango_credential.app.core.config import Settings
from ango_credential.app.core.exceptions import AuthException
from ango_credential.app.middleware.auth import authorize_service, authorize_user, parse_token
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


@credential_router.get("/user/{user_id}", dependencies=[Depends(authorize_user)])
def get_credentials(user_id: str, token_data: TokenData = Depends(parse_token)) -> List[CredentialDb] | None:
    if user_id != token_data.user_id:
        raise AuthException(message="User not authorized")

    credentials = credential_service.get_credential_by_user_id(user_id=token_data.user_id)
    return credentials


@credential_router.post("/")
def create_credential(create_request: CredentialCreateRequest) -> CredentialDb:
    credential = credential_service.create(create_request)
    return credential


@credential_router.get("/", dependencies=[Depends(authorize_service), Depends(authorize_user)])
def get_user_by_domain_name(domain_name: str) -> CredentialDb:
    credential = credential_service.get_credential_by_domain_name(domain_name=domain_name)
    return credential


@credential_router.put("/", dependencies=[Depends(authorize_service), Depends(authorize_user)])
def update_credential(request: CredentialUpdateRequest):
    credential_service.update(request)
    return "Credential updated"


@credential_router.delete("/", dependencies=[Depends(authorize_user), Depends(authorize_service)])
def delete_user(request: CredentialDeleteRequest):
    credential_service.delete(request)
    return "Credential deleted"
