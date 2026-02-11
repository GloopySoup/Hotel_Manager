import os
from google import genai
from dotenv import load_dotenv, dotenv_values 
from sqlalchemy import Table,Column,MetaData,Text,Integer,create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from fastapi import FastAPI

load_dotenv()
app = FastAPI()


client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))
engine = create_engine("mysql+aiomysql://root:Red47red.@localhost:3306/hotelmanager")
SessionLocal = sessionmaker(autoflush=False,bind=engine)

Base = declarative_base()
