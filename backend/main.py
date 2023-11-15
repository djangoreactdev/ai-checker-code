import docs

import uvicorn
from fastapi import FastAPI, HTTPException
import restapi.router
from fastapi.middleware.cors import CORSMiddleware
from loguru import logger
from restapi import events


app = FastAPI(title="Code checker API", description=docs.desc)


# CORS Configuration (in-case you want to deploy)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["GET", "POST", "OPTIONS"],
    allow_headers=["*"],
)

logger.info("Adding v1 endpoints..")

# add v1
restapi.router.configure(app)

app.add_event_handler("startup", events.startup_event_handler(app))

app.add_event_handler("shutdown", events.shutdown_event_handler())

app.add_exception_handler(HTTPException, events.on_http_error)


def main():
    uvicorn.run(app, host="0.0.0.0", port=8000)


if __name__ == "__main__":
    main()
