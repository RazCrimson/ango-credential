from fastapi import Cookie, Request
from jose import JWTError, jwt
from pydantic import ValidationError

from ango_credential.app.core.config import Settings
from ango_credential.app.core.exceptions import AuthException
from ango_credential.app.models.auth import TokenData

settings = Settings()


def parse_token(access_token: str = Cookie(...)) -> TokenData:
    try:
        payload = jwt.decode(access_token, settings.SECRET_KEY, algorithms=[settings.ALGORITHM])
        token_data = TokenData.parse_obj(payload)
        return token_data

    except (JWTError, ValidationError):
        raise AuthException(message="Invalid token")


def authorize_user(access_token: str = Cookie(...)) -> None:
    token_data = parse_token(access_token)
    # if token_data.email != request.email:
    #     raise AuthException(message="Unauthorized user")


def authorize_service(shared_secret: str = Cookie(...)):
    if shared_secret != settings.SHARED_ACCESS_TOKEN:
        raise AuthException(message="Unauthorized service")


def check_auth(request: Request):
    shared_secret = request.cookies.get("shared_secret")
    access_token = request.cookies.get("access_token")

    if not shared_secret and not access_token:
        raise AuthException(message="Unauthorized")

    if shared_secret:
        # Give precedence to shared secret over access token
        if shared_secret != settings.SECRET_KEY:
            raise AuthException(message="Unauthorized service")
    else:
        # No shared secret, check access token
        parse_token(access_token)
