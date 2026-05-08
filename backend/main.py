from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session  

from database import SessionLocal, engine, Base
import models
import schemas


Base.metadata.create_all(bind=engine)

app = FastAPI()

# Dependency to get DB session 
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
        

@app.get("/")
def home():
    return {"message": "Backend is running!"}
