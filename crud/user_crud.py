from sqlalchemy.orm import Session
from schema.user import UserCreate, UserBase, UserLogin
from model.user_model import User
from hashing import hash_password, verify_password

def create_user(db: Session, user: UserCreate):
    hashed_password = hash_password(user.password)
    db_user = User(username=user.username, email=user.email, password_hash=hashed_password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def get_all_user(db: Session):
    return db.query(User).all()

def get_user_by_username(db: Session, username: str):
    return db.query(User).filter(User.username == username).first() 
    # ekta database er username column er value ta username er value er shate match korbe
     
def get_user_by_email(db: Session, email: str):
    return db.query(User).filter(User.email == email).first()

def verify_password(plain_password, hashed_password):
    isVerified = verify_password(plain_password, hashed_password)
    # Add your password verification logic here
    # For example, you can use a hashing library to compare passwords
    return isVerified  # Placeholder implementation, replace with actual logic
