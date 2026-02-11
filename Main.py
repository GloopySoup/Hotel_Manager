import os
from google import genai
from dotenv import load_dotenv, dotenv_values 
from sqlalchemy import Table,Column,MetaData,Text,Integer,create_engine
load_dotenv()

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

