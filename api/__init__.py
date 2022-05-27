from typing import *
from pymongo import MongoClient
import uvicorn
from fastapi import FastAPI, Request, Response, status
from fastapi.responses import JSONResponse, PlainTextResponse
from fastapi.exceptions import ValidationError
from .routers import ROUTERS

app = FastAPI(
    title="EMPLOYEE-SERVICE",
)

# @app.on_event("startup")
# async def startup_event():
#     db.initialize()
   

for router in ROUTERS:
    app.include_router(router)


def serve() -> None:
    uvicorn.run(app, host="localhost", port="8002")