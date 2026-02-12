from sqlalchemy import Table, Column, Integer, String, MetaData
from main import Base, hotel_name
MetaData = MetaData()

class Hotel(Base):
    __tablename__ = "koala hotels",
    customerID =Column(Integer, primary_key=True, index=True)
