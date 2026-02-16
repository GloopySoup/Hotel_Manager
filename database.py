import os
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base, Session
from sqlalchemy import Table, Column, Integer, String, MetaData
from typing import Annotated, Optional, List
import config
import gemini

SessionLocal = None
def start_db():
    load_dotenv()
    engine = create_engine(os.getenv("DATABASE_URL"))
    SessionLocal = sessionmaker(autocommit=False,autoflush=False,bind=engine)
    Base = declarative_base()

    class Hotel(Base):
        __tablename__ = gemini.ai(input(">"))
        customerID = Column(Integer, primary_key=True, index=True)
        customerName = Column(String(50),index=True)

    Base.metadata.create_all(engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()




