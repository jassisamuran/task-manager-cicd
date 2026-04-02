from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

class AuthMethod(BaseModel):
    method: str
    endpoint: str

# Sample authentication methods
authentication_methods = [
    AuthMethod(method="JWT", endpoint="/auth/jwt"),
    AuthMethod(method="OAuth2", endpoint="/auth/oauth2"),
    AuthMethod(method="Basic", endpoint="/auth/basic"),
]

@app.get("/auth/methods")
def get_auth_methods():
    return authentication_methods

@app.post("/auth/methods")
def add_auth_method(auth_method: AuthMethod):
    authentication_methods.append(auth_method)
    return auth_method
