from fastapi import FastAPI
from app.api.v1 import api
from app.core.config import settings

app = FastAPI(title=settings.PROJECT_NAME, openapi_url=f"{settings.API_V1_STR}/openapi.json")
app.include_router(api.router, prefix=settings.API_V1_STR)




@app.get("/")
async def root():
    return {"message": "Welcome to the E-commerce API!"}