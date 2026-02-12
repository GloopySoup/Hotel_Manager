import os
from google import genai
from dotenv import load_dotenv, dotenv_values 
from sqlalchemy import Table,Column,MetaData,Text,String,Integer,create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, declarative_base
from fastapi import FastAPI

load_dotenv()
app = FastAPI()


client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))
engine = create_engine(os.getenv("DATABASE_URL"))
Session = sessionmaker(bind=engine)
session = Session()

Base = declarative_base()

#Generates content to fill the sql query to create a database table
def generate_query():
    response = client.models.generate_content(
        model="gemini-3-flash-preview",
        contents="Generate an sql query using sqlalchemy in python to create a table in mysql for my hotel called koalaHotels"
    )
    print(response.text)



generate_query()