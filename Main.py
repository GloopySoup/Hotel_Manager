import os
import json
import gemini
from dotenv import load_dotenv
from fastapi import FastAPI, HTTPException, Depends, status
from pydantic import BaseModel
from typing import Annotated, Optional, List
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base, Session
from sqlalchemy import Table, Column, Integer, String, MetaData

load_dotenv()
app = FastAPI()

engine = create_engine(os.getenv("DATABASE_URL"))
SessionLocal = sessionmaker(autocommit=False,autoflush=False,bind=engine)
Base = declarative_base()






hotelTable_name = gemini.ai("Hey, i'd like to register with your hotel management system. We're called Koala Hotels and have 3 different types of Rooms: Large, Medium, Small")


class Hotel(Base):
    __tablename__ = "koala hotels"
    customerID = Column(Integer, primary_key=True, index=True)
    customerName = Column(String(50),index=True)

Base.metadata.create_all(engine)

class CustomerCreate(BaseModel):
    customerID : int
    customerName : str

class UserResponse(BaseModel):
    customerID: int
    customerName: str

    class config:
        orm_mode = True

class CustomerUpdate(BaseModel):
    customerName : Optional[str]

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

db_dependency = Annotated[Session, Depends(get_db)]

@app.delete("/customers/{customerID}",status_code=status.HTTP_200_OK)
async def delete_customer(customerID: int, db: db_dependency):
    db_customer = db.query(Hotel).filter(Hotel.customerID == customerID).first()
    if db_customer is None:
        raise HTTPException(status_code=404, detail='Customer was not found')
    db.delete(db_customer)
    db.commit()

@app.post("/customers/", response_model=UserResponse)
async def create_customer(customer: CustomerCreate, db: db_dependency):
    db_customer = Hotel(**customer.dict())
    db.add(db_customer)
    db.commit()
    db.refresh(db_customer)
    return db_customer

@app.get("/customers/{customerID}",response_model=UserResponse)
async def read_customer(customerID: int, db: db_dependency):
    db_customer = db.query(Hotel).filter(Hotel.customerID == customerID).first()
    if db_customer is None:
        raise HTTPException(status_code=404, detail='Customer not found')
    return db_customer

@app.put("/customers/{customerID}", response_model=UserResponse)
async def update_customer(customerID: int, customer: CustomerUpdate, db: db_dependency):
    db_customer = db.query(Hotel).filter(Hotel.customerID == customerID).first()
    if db_customer is None:
        raise HTTPException(status_code=404, detail="Customer not found")
    db_customer.customerName = Hotel.customerName if Hotel.customerName is not None else db_customer.customerName
    db.commit()
    db.refresh(db_customer)
    return db_customer 
    

    


