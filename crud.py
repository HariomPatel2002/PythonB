from sqlalchemy.orm import Session
from models import User

def create_user(db: Session, name: str, email: str, age: int = None):
    user = User(name=name, email=email, age=age)  # Include age here
    db.add(user)
    db.commit()
    db.refresh(user)
    return user

def get_users(db: Session):
    return db.query(User).all()

def update_user(db: Session, user_id: int, new_email: str = None, new_age: int = None):
    user = db.query(User).filter(User.id == user_id).first()
    if user:
        if new_email:
            user.email = new_email
        if new_age is not None:
            user.age = new_age
        db.commit()
        db.refresh(user)
        return user

def delete_user(db: Session, user_id: int):
    user = db.query(User).filter(User.id == user_id).first()
    if user:
        db.delete(user)
        db.commit()
