from components.core.settings import settings
from fastapi import HTTPException
from fastapi.responses import JSONResponse
from starlette.requests import Request
from loguru import logger


startup_msg_fmt = "Starting ai checker code"


async def on_http_error(request: Request, exc: HTTPException):
    return JSONResponse({"detail": exc.detail}, status_code=exc.status_code)


async def on_startup(app):
    startup_msg = startup_msg_fmt.format(settings=settings)
    logger.info(startup_msg)


def startup_event_handler(app):
    if settings.sentry_dns is not None:
        import sentry_sdk

        def traces_sampler(sampling_context):
            if "health" in sampling_context["transaction_context"]["name"]:
                return False

        sentry_sdk.init(
            dsn=settings.sentry_dns,
            traces_sample_rate=0.1,
            traces_sampler=traces_sampler,
            send_default_pii=False,
        )

    async def start_app() -> None:
        await on_startup(app)

    return start_app


async def shutdown():
    logger.info("Shutting down API")


def shutdown_event_handler():
    async def start_app() -> None:
        await shutdown()

    return start_app
