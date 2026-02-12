import os
import json
from google import genai
from dotenv import load_dotenv, dotenv_values 
from sqlalchemy import create_engine, Table, Column, Integer, String, MetaData
from sqlalchemy.orm import sessionmaker, declarative_base


load_dotenv()

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

engine = create_engine(os.getenv("DATABASE_URL"))
engine.connect()
Session = sessionmaker(bind=engine)
Base = declarative_base()
metadata = MetaData()

def create_hotel_table(user_input):
    response = client.models.generate_content(
        model="gemini-3-flash-preview",
        contents="""Extract structured data from the text below.

        Return ONLY valid JSON in this format:
        {{
        "hotel_name": "string",
        "room_type": "string"
        }}
    Text: """ + user_input,
    config={"response_mime_type": "application/json"})

    data = json.loads(response.text)
    hotel_name = int(data["hotel_name"])
    hotel_table = Table(hotel_name,
                        metadata,
                        Column("customerID", Integer, primary_key=True))
    metadata.create_all(engine)

create_hotel_table(input">")