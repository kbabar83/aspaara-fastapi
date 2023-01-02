from app.routers import router
from fastapi import FastAPI
from app import models
from config.database import engine
from fastapi_pagination import add_pagination


models.Base.metadata.create_all(bind=engine)

app = FastAPI(title="Aspaara API")
app.include_router(router, prefix="/app")

add_pagination(app)
