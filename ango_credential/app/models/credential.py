from datetime import datetime
from typing import Optional
from uuid import UUID

from pydantic import BaseModel


class CredentialBase(BaseModel):
    user_id: UUID
    pass_encrypted: bytes


class CredentialCreateRequest(CredentialBase):
    """
    User is not required to send both domain and name
    If there is no domain, then user must send name
    If there is a domain in the request and no name, set name = domain
    """

    name: Optional[str] = None
    domain: Optional[str] = None
    username: Optional[str] = None


class CredentialCreate(CredentialBase):
    name: str
    username: Optional[str]
    domain: Optional[str]
    created_at: datetime


class CredentialUpdateRequest(BaseModel):
    user_id: UUID
    id: UUID
    name: str
    username: str
    domain: str
    pass_encrypted: bytes


class CredentialDbBase(CredentialBase):
    id: UUID
    domain: Optional[str] = None
    name: str
    username: Optional[str] = None
    created_at: datetime
    updated_at: Optional[datetime] = None

    class Config:
        orm_mode = True


class Credential(CredentialDbBase):
    pass


class CredentialDb(CredentialDbBase):
    pass


class CredentialDeleteRequest(BaseModel):
    id: UUID
