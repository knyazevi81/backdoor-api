from sqlalchemy import create_engine
from sqlalchemy.orm import Session, sessionmaker
from models import Computer


engine = create_engine("sqlite:///backdoor.db", echo=True)


class Database:
    
    def __init__(self):
        SessionLocal = sessionmaker(autoflush=False, bind=engine)
        self.db = SessionLocal()

    
    def create_user(self, name: str):
        self.db.add(Computer(
            pc_name = name ,
            status_id = 0,
            status = "none",
        ))
        self.db.commit()

if __name__ == "__main__":
    Database().create_user(name="ilpdakz")