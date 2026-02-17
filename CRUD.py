import database
import config
import SQLrepository
from fastapi import  HTTPException, Depends, APIRouter
from typing import Annotated



db_dependency = database.Annotated[database.Session, Depends(database.get_db)]
router = APIRouter()



@router.delete("/customers/{customerID}",response_model=config.UserResponse)
async def delete_customer(customerID: int, db: db_dependency):
    db_customer = SQLrepository.query(db, customerID)
    if db_customer is None:
        raise HTTPException(status_code=404, detail='Customer was not found')
    db.delete(db_customer)
    db.commit()
    return db_customer

@router.post("/customers/", response_model=config.UserResponse)
async def create_customer(customer: config.CustomerCreate, db: db_dependency):
    db_customer = database.Hotel(**customer.model_dump())
    db.add(db_customer)
    db.commit()
    db.refresh(db_customer)
    return db_customer

@router.get("/customers/{customerID}",response_model=config.UserResponse)
async def read_customer(customerID: int, db: db_dependency):
    db_customer = SQLrepository.query(db, customerID)
    if db_customer is None:
        raise HTTPException(status_code=404, detail='Customer not found')
    return db_customer

@router.put("/customers/{customerID}", response_model=config.UserResponse)
async def update_customer(customerID: int, customer: config.CustomerUpdate, db: db_dependency):
    db_customer = SQLrepository.query(db, customerID)
    if db_customer is None:
        raise HTTPException(status_code=404, detail="Customer not found")
    if customer.customerName is not None:
        db_customer.customerName = customer.customerName
    db.commit()
    db.refresh(db_customer)
    return db_customer 