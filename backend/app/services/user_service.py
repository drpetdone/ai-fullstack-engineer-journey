from sqlalchemy.orm import Session
from app.models.user import User

def create_user(db: Session, user_data):
    user = User(
        name=user_data.name, 
        email=user_data.email
    )

    db.add(user)
    db.commit()
    db.refresh(user)
    return user

def get_all_users(db: Session):
    return db.query(User).all()

def get_user_by_id(db: Session, user_id: int):
    return db.query(User).filter(User.id == user_id).first()

def delete_user(db: Session, user):
    db.delete(user)
    db.commit()

def update_user(db: Session, user, user_data):
    user.name = user_data.name
    user.email = user_data.email
    db.commit()
    db.refresh(user)
    return user 
