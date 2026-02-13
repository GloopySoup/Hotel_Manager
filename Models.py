from sqlalchemy import Table, Column, Integer, String, MetaData
from database import Base
from main import hotel_name

class Hotel(Base):
    __tablename__ = hotel_name,
    customerID =Column(Integer, primary_key=True, index=True)
