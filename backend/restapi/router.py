import fastapi
from restapi.routes import ai_router, health


def configure(app: fastapi.FastAPI):
    router = fastapi.APIRouter(prefix="/api/v1")
    router.include_router(health.router)
    router.include_router(ai_router.router)
    return app.include_router(router)
