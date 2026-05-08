from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database import SessionLocal
from app.schemas.user_schema import UserCreate, UserResponse
from app.services.user_service import(
    create_user,
    get_all_users,
    get_user_by_id,
    delete_user,
    update_user
)

router = APIRouter()

# Dependency to get DB session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# create_user    
@router.post("/users/", response_model=UserResponse)
def create_new_user(user: UserCreate, db: Session = Depends(get_db)):
    return create_user(db, user)

# get_all_users
@router.get("/users/", response_model=list[UserResponse])
def fetch_users(db: Session = Depends(get_db)):
    return get_all_users(db)

# get_user_by_id
@router.get("/users/{user_id}", response_model=UserResponse)
def fetch_user(user_id: int, db: Session = Depends(get_db)):
    user = get_user_by_id(db, user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user

# delete_user
@router.delete("/users/{user_id}")
def remove_user(user_id: int, db: Session = Depends(get_db)):
    user = get_user_by_id(db, user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    delete_user(db, user)
    return {"message": "User deleted"}   

# modify_user
@router.put("/users/{user_id}", response_model=UserResponse)
def modify_user(user_id: int, user_data: UserCreate, db: Session = Depends(get_db)):
    user = get_user_by_id(db, user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return update_user(db, user, user_data) 

