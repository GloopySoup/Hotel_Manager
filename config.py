from typing import  Optional
from pydantic import BaseModel
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

