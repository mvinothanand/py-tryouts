from datetime import timedelta, datetime, timezone

import jwt #pip install pyjwt
from jwt.exceptions import InvalidTokenError
from fastapi import FastAPI, Depends, HTTPException, status
# fastapi.security module has all the modules related to security
# Oauth2PasswordBearer - to define the Password flow OAuth scheme
# OAuth2PasswordRequestForm - to handle the form data with username/password
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm, APIKeyCookie, APIKeyHeader
from typing import Annotated
from pydantic import BaseModel

#Global variables
#generate the secret key using:
# openssl rand -hex 32
SECRET_KEY="0e47be9fb6fec810a7a33a3bad16a15e18daebd134685c5a10d61693f85b0ee1"
ALGORITHM="HS256"
ACCESS_TOKEN_EXPIRY_IN_MINUTES=30

fake_users_db = {
  "vinoth": {
     "username": "vinoth",
     "apikey": "vinothanandabcdegh1223j23kj4"
  },
  "anand": {
    "username": "anand"
  }
}

fake_api_keys = [
  "abcdef",
  "xyz"
]

# create a fastapi app
app = FastAPI()

# define the oauth2 scheme
# OAuth Password flow
# the tokenUrl has the relative url (to this app) which handles the OAuth and returns a token
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token") 

#defining an apiKey scheme
# api_key_cookie_scheme = APIKeyCookie(name="api_key")
api_key_header_scheme = APIKeyHeader(name="api_key")
# use api key for login alone and later use a JWT token
api_key_oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token_api_key")

# Pydantic class for Token to be sent in the login endpoint
class Token(BaseModel):
  access_token: str
  token_type: str


#Pydantic model for token data
class TokenData(BaseModel):
  username: str | None = None


#create access token
def create_access_token(data: dict, expires_in: timedelta | None = None):
  to_encode = data.copy()
  if expires_in:
    expire = datetime.now(timezone.utc) + expires_in
  else:
    expire = datetime.now(timezone.utc) + timedelta(minutes=ACCESS_TOKEN_EXPIRY_IN_MINUTES)

  to_encode.update({ "exp": expire})
  encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
  
  return encoded_jwt


# path for login with username and password
@app.post("/token")
async def login(form_data: Annotated[OAuth2PasswordRequestForm, Depends()]):
  print(f"Input username: {form_data.username}")
  user = fake_users_db.get(form_data.username)
  if not user:
    raise HTTPException(status_code=400, detail="Invalid user")
  
  print(f"fetched user: {user}")
  # create access token
  access_token_expires_in = timedelta(minutes=ACCESS_TOKEN_EXPIRY_IN_MINUTES)
  access_token = create_access_token(
    data = { "sub": user["username"]},
    expires_in=access_token_expires_in
  )
  
  print(f"Access Token: {access_token}")
  return Token(access_token=access_token, token_type="bearer")


# path for login with api key and get an access token
@app.post("/token_api_key")
async def login_with_api_key(api_key: str = Depends(api_key_header_scheme)):
  print(f'provided api key: {api_key}')
  
  if not api_key in fake_api_keys:
    raise HTTPException(status_code=400, detail="Invalid key")
  
  #create access token
  access_token_expires_in = timedelta(minutes=ACCESS_TOKEN_EXPIRY_IN_MINUTES)
  access_token = create_access_token(
    data = {"sub": 'tci-frontend'},
    expires_in=access_token_expires_in
  )

  print(f'Access token: {access_token}')
  return Token(access_token=access_token, token_type='bearer')


# get current user
async def get_current_user(token: Annotated[str, Depends(oauth2_scheme)]):
  credentials_exception = HTTPException(
    status_code=status.HTTP_401_UNAUTHORIZED,
    detail="Could not validate credentials",
    headers={"WWW-Authenticate": "Bearer"}
  )

  try:
    payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
    username = payload.get("sub")
    
    if username is None:
      raise credentials_exception
    
    token_data = TokenData(username=username)
  except InvalidTokenError:
    raise credentials_exception
  
  user = fake_users_db[token_data.username]
  if user is None:
    raise credentials_exception
    
  print(f"user is: {user}")
  return user


@app.get("/")
async def hello(username: Annotated[str, Depends(get_current_user)]):
  if username:
    return {"message": "hello"}
  else:
    return {"message": "invalid user"}
  

@app.get("/getInfo")
async def get_info(api_key: str = Depends(api_key_header_scheme)):
  print(api_key)
  if api_key in fake_api_keys:
    return {"message": "successfully logged in"}
  else:
    return {"message": "invalid api key"}
  

@app.get("/getList")
async def get_list(token: Annotated[str, Depends(api_key_oauth2_scheme)]):
  if token:
    print(f'token is: {token}')
    return {
      "message": "success",
      "values": [1, 2, 3]
    }
  else:
    return {
      "message": "not authorized"
    }

