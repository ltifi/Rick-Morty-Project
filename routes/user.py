from fastapi import APIRouter, Depends, HTTPException
from fastapi_pagination import  Page, add_pagination, paginate
from config.database import SessionLocal
from fastapi.security import OAuth2PasswordRequestForm
from datetime import timedelta
from starlette.status import HTTP_401_UNAUTHORIZED
import config.config 
from fastapi.responses import RedirectResponse, HTMLResponse
from crud.user import add_user,get_all_users
from models.user import User
from schemas.user import UserSchema, UserCreateSchema, user
from security.security import get_user_by_email, authenticate_user, create_access_token


app = APIRouter()
session=SessionLocal()

ACCESS_TOKEN_EXPIRE_MINUTES=config.config.Settings().ACCESS_TOKEN_EXPIRE_MINUTES

@app.post("/signUp", response_model=UserSchema)
def sign_up(user_data: UserCreateSchema):
    user = get_user_by_email(session, user_data.email)
    if user:
        raise HTTPException(
            status_code=409,
            detail="email exist",
        )
    new_user = add_user(session, user_data)
    return new_user
    

@app.post("/login", response_class=HTMLResponse)
def login_for_access_token(
        form_data: OAuth2PasswordRequestForm = Depends()
):
    user_data = authenticate_user(form_data.username, form_data.password)
    if not user_data:
        raise HTTPException(
            HTTP_401_UNAUTHORIZED,
            detail="invalid email or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    token_expires_date = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={'sub': user_data.email},
        expires_delta=token_expires_date,
    )
    response = RedirectResponse('/episodes/page', status_code=303)
    response.set_cookie(key="session_token", value=access_token)
    return response


@app.post("/logout",response_class=HTMLResponse)
def logout():
  response = RedirectResponse('/', status_code= 302)
  response.delete_cookie(key="session_token")
  return response

@app.get("/user", response_model=user)
async def get_user(id:int):
    db_user = session.query(User).get(id)
    return db_user

@app.get("/users", response_model=Page[UserSchema])
async def get_characters():
    db_users = get_all_users(session)
    return paginate(db_users)

@app.delete("/user")
def delete_user_info(id: int):
    user_info = session.query(User).get(id)
    session.delete(user_info)
    session.commit()
    return {'message': 'The user is deleted successfully'}

@app.put("/user")
async def update_user_lastname(id: int, username_update: UserSchema)->User:
    username_info = session.query(User).get(id)
    username_info.lastName = username_update.lastName
    username_info.firstName = username_update.firstName
    username_info.email = username_update.email
    session.commit()
    session.refresh(username_info)
    return username_info

add_pagination(app)