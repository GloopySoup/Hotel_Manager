from typing import  Optional
from pydantic import BaseModel

class CustomerCreate(BaseModel):
    customerName : str

class UserResponse(BaseModel):
    customerID: int
    customerName: str

    class Config:
        from_attributes = True

class CustomerUpdate(BaseModel):
    customerName : Optional[str]

