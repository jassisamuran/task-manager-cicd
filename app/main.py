from fastapi import FastAPI
from app.api.routes.signin import router as signin_router

app = FastAPI()

app.include_router(signin_router)

@app.get("/")
async def root():
    return {"message": "Hello World"}