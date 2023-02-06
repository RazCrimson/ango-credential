import uvicorn
from fastapi import FastAPI

from ango_credential.app.core.config import Settings
from ango_credential.app.routers.credential import credential_router

settings = Settings()

app = FastAPI(
    title="Ango - Credential microservice",
    docs_url=f"{settings.APP_PREFIX.rstrip('/')}/docs",
    redoc_url=f"{settings.APP_PREFIX.rstrip('/')}/redoc",
    openapi_url=f"{settings.APP_PREFIX.rstrip('/')}/openapi.json",
)

app.include_router(credential_router, prefix=f"{settings.APP_PREFIX.rstrip('/')}/v1", tags=["Credential API V1"])

if __name__ == "__main__":
    uvicorn.run(app, host=settings.SERVER_HOST, port=settings.SERVER_PORT)
