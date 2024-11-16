from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from jose import JWTError, jwt
from datetime import datetime, timedelta
from sqlalchemy.orm import Session
from . import crud, models, schemas, database

SECRET_KEY = "your-secret-key"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

def authenticate_professor(db: Session, email: str, password: str):
    professor = crud.get_professor_by_email(db, email)
    if not professor:
        return False
    if not crud.verify_password(password, professor.hashed_password):
        return False
    return professor