from fastapi import FastAPI,HTTPException
from fastapi.exceptions import RequestValidationError
from app.db.database import Base,engine
from app.core.exceptions import validation_exception_handler,http_exception_handler
from app.models.user import User
from app.models.research_project import research_member,research_projects
from app.models.research_task import research_task


app = FastAPI(
    title="RESEARCH GROUP MANAGEMENT API"
)

Base.metadata.create_all(bind=engine)

app.add_exception_handler(HTTPException, http_exception_handler)
app.add_exception_handler(RequestValidationError, validation_exception_handler)


@app.get("/")
def get_root():
    return {
        "message":"Connection Complete"
    }
