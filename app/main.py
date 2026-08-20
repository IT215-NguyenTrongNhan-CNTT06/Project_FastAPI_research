from fastapi import FastAPI, HTTPException
from fastapi.exceptions import RequestValidationError
from app.db.database import Base, engine
from app.core.exceptions import validation_exception_handler, http_exception_handler
from app.routers import health
import app.models


app = FastAPI(
    title="RESEARCH GROUP MANAGEMENT API" 
)

Base.metadata.create_all(bind=engine)


app.add_exception_handler(HTTPException, http_exception_handler)
app.add_exception_handler(RequestValidationError, validation_exception_handler)


app.include_router(health.router)