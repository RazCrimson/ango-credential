import uvicorn
from fastapi import FastAPI

from ango_credential.app.core.config import Settings
from ango_credential.app.routers.user import user_router

settings = Settings()

app = FastAPI()

app.include_router(user_router, prefix="/credential")

uvicorn.run(app, host=settings.SERVER_HOST, port=settings.SERVER_PORT)
