from fastapi import FastAPI
from app.api.routes import signin

app = FastAPI()

app.include_router(signin.router)

@app.get("/")
async def root():
    return {"message": "Hello World"}