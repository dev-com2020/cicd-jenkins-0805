from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from . import models, crud, database

models.Base.metadata.create_all(bind=database.engine)
app = FastAPI()

def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/users")
def create_user(name: str, db: Session = Depends(get_db)):
    return crud.create_user(db, name)

@app.get("/users/{user_id}")
def read_user(user_id: int, db: Session = Depends(get_db)):
    return crud.get_user(db, user_id)
