from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from models import Computer


engine = create_engine("sqlite:///backdoor.db", echo=True)


class Database:
    
    def __init__(self):
        with Session(autoflush=False, bind=engine) as db:
            self.db = Session(autoflush=False, bind=engine)

    
    def create_user(self, name: str, status: int = 0):
        self.db.add(Computer(
            name=name,
            status=status
        ))
        self.db.commit()


class DatabaseTest:
    
    def create_user(self, name: str, status: int = 0):
        with Session(autoflush=False, bind=engine) as db:
            db.add(Computer(name=name, status=status))     # добавляем в бд
            db.commit()     # сохраняем изменения

if __name__ == "__main__":
    DatabaseTest.create_user("t6est", 12)