from sqlalchemy import create_engine
from sqlalchemy.orm import Session, sessionmaker
from models import Computer
from time import sleep


engine = create_engine("sqlite:///backdoor.db")


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

    def read_pc_status(self):
        pcs = self.db.get(Computer, 1)
        print([pcs.id, pcs.pc_name])

if __name__ == "__main__":
    #Database().create_user(name="petya")
    for i in range(100):
        sleep(1)
        Database().read_pc()