from sqlalchemy import Table, Column, Integer, String, MetaData
from Main import Base, hotel_name
meta = MetaData()
class Hotel(Base):
    __tablename__ = hotel_name,
    customerID =Column(Integer, primary_key=True, index=True)
