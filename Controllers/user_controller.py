from sqlalchemy.orm import Session
from app.Models.users import UserDB

def create_user(db: Session, username: str, password: str, is_admin: bool):
    user = UserDB(username=username, password=password, is_admin=is_admin)
    db.add(user)
    db.commit()
    return user

def get_user(db: Session, username: str):
    return db.query(UserDB).filter(UserDB.username == username).first()
