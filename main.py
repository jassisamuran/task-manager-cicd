from fastapi import FastAPI, Depends
from fastapi.security import OAuth2PasswordRequestForm
from auth import Auth
from schemas import UserCreate, UserResponse
from dependencies import get_current_user

app = FastAPI()

auth = Auth()

@app.post('/token')
async def login(form_data: OAuth2PasswordRequestForm = Depends()):
    user = auth.verify_user(form_data.username, form_data.password)
    if not user:
        raise HTTPException(status_code=400, detail='Incorrect username or password')
    access_token = auth.create_access_token(data={'sub': user.username})
    return {'access_token': access_token, 'token_type': 'bearer'}

@app.get('/users/me', response_model=UserResponse)
async def read_users_me(current_user: str = Depends(get_current_user)):
    return current_user
