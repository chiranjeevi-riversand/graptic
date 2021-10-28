from fastapi import FastAPI

from ticketService.app.api.api import tic

app = FastAPI(openapi_url="/api/v1/tic/openapi.json", docs_url="/api/v1/tic/docs")

@app.on_event("startup")
def startup():
    return 0

@app.on_event("shutdown")
def shutdown():
    return 0

app.include_router(tic, prefix='/api/v1/tic')