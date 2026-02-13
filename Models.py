from sqlalchemy import Table, Column, Integer, String, MetaData
from database import Base

class Hotel(Base):
    __tablename__ = "koala hotels",
    customerID =Column(Integer, primary_key=True, index=True)
