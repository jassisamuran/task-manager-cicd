from fastapi import Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer
from auth import Auth

oauth2_scheme = OAuth2PasswordBearer(tokenUrl='token')

def get_current_user(token: str = Depends(oauth2_scheme)):
    auth = Auth()
    payload = auth.decode_access_token(token)
    return payload
