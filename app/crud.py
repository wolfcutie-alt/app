from sqlalchemy.orm import Session
<<<<<<< HEAD
=======
from models import User
>>>>>>> b9abe0142f4ce09b1438de10ba116ec7638e27fa

class UserCRUD:
    @staticmethod
    def create_user(db: Session, username: str, email: str):
        db.execute(
            "INSERT INTO users (username, email) VALUES (:username, :email)",
            {"username": username, "email": email}
        )
        db.commit()

    @staticmethod
    def get_user(db: Session, user_id: int):
        return db.execute(
            "SELECT * FROM users WHERE id = :user_id",
            {"user_id": user_id}
        ).fetchone()

    @staticmethod
    def update_user(db: Session, user_id: int, username: str, email: str):
        db.execute(
            "UPDATE users SET username = :username, email = :email WHERE id = :user_id",
            {"username": username, "email": email, "user_id": user_id}
        )
        db.commit()

    @staticmethod
    def delete_user(db: Session, user_id: int):
        db.execute(
            "DELETE FROM users WHERE id = :user_id",
            {"user_id": user_id}
        )
        db.commit()
