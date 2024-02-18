from sqlalchemy.orm import DeclarativeBase
from sqlalchemy import Column, Integer, String
from sqlalchemy import create_engine

engine = create_engine("sqlite:///backdoor.db", echo=False)


class Base(DeclarativeBase):
    pass


class Computer(Base):
    __tablename__= "computers"

    id = Column(Integer, primary_key=True, index=True)
    pc_name = Column(String)
    status_id = Column(Integer)
    status = Column(Integer)


Base.metadata.create_all(bind=engine)