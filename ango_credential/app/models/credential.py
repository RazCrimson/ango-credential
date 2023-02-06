from datetime import datetime
from typing import Optional
from uuid import UUID

from pydantic import BaseModel


class CredentialBase(BaseModel):
    user_id: UUID
    pass_encrypted: bytes


class CredentialCreateRequest(CredentialBase):
    name: str
    domain_name: str
    user_id: UUID


class CredentialUpdateRequest(BaseModel):
    user_id: str
    id: str
    name: str
    domain_name: str
    pass_encrypted: bytes


class CredentialCreate(CredentialBase):
    name: str
    domain_name: str
    created_at: datetime


class CredentialDbBase(CredentialBase):
    id: UUID
    domain_name: str
    name: str
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True


class Credential(CredentialDbBase):
    pass


class CredentialDb(CredentialDbBase):
    pass


class CredentialDeleteRequest(BaseModel):
    id: UUID
