from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from schema.user import UserCreate, UserLogin
from crud import user_crud
from database import SessionLocal
from hashing import verify_password

router = APIRouter()

# Dependency to get the database session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/signup/")
def signup(user: UserCreate, db: Session = Depends(get_db)):
    db_user = user_crud.get_user_by_username(db, username=user.username)
    if db_user:
        raise HTTPException(status_code=400, detail="Username already registered")
    db_user = user_crud.get_user_by_email(db, email=user.email)
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    return user_crud.create_user(db=db, user=user)

@router.get("/user/")
def getalluser(db: Session = Depends(get_db)):
    return user_crud.get_all_user(db)

@router.get("/user/{user_name}")
def getuserbyusername(user_name: str, db: Session = Depends(get_db)):
    db_user = user_crud.get_user_by_username(db, username=user_name)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user

@router.post("/login/")
def login(user: UserLogin, db: Session = Depends(get_db)):
    db_user = user_crud.get_user_by_username(db, username=user.username)
    if not db_user:
        raise HTTPException(status_code=401, detail="Invalid username or password")
    if not verify_password(user.password, db_user.password_hash):
        raise HTTPException(status_code=401, detail="Invalid username or password")
    # Add your authentication logic here, e.g., generate JWT token, set session, etc.
    return {"message": "Login successful"}
