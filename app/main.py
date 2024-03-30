from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy.orm import Session
<<<<<<< HEAD
from .crud import UserCRUD
from .database import SessionLocal
=======
import crud, models, database
>>>>>>> b9abe0142f4ce09b1438de10ba116ec7638e27fa

app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/users/")
def create_user(username: str, email: str, db: Session = Depends(get_db)):
    UserCRUD.create_user(db, username, email)
    return {"message": "User created successfully"}

@app.get("/users/{user_id}")
def read_user(user_id: int, db: Session = Depends(get_db)):
    user = UserCRUD.get_user(db, user_id)
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return dict(user)

@app.put("/users/{user_id}")
def update_user(user_id: int, username: str, email: str, db: Session = Depends(get_db)):
    UserCRUD.update_user(db, user_id, username, email)
    return {"message": "User updated successfully"}

@app.delete("/users/{user_id}")
def delete_user(user_id: int, db: Session = Depends(get_db)):
    UserCRUD.delete_user(db, user_id)
    return {"message": "User deleted successfully"}
