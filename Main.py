import os
import json
from dotenv import load_dotenv
from google import genai
from fastapi import FastAPI, HTTPException, Depends, status
from pydantic import BaseModel
from typing import Annotated
import models
from database import engine, SessionLocal
from sqlalchemy.orm import Session

load_dotenv()
client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))
app = FastAPI()

models.Base.metadata.create_all(bind=engine)

class CustomerBase(BaseModel):
    customerID: int

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

db_dependency = Annotated[Session, Depends(get_db)]

@app.post("/customers/", status_code=status.HTTP_201_CREATED)
async def create_customer(customer: CustomerBase, db: db_dependency):
    db_customer = models.Hotel(**customer.dict())
    db.add(db_customer)
    db.commit()


def ai():

    pass
    #response = client.models.generate_content(
        #model="gemini-3-flash-preview",
        #contents="""Extract structured data from the text below.

        #Return ONLY valid JSON in this format:
        #{{
        #"hotel_name": "string",
        #"room_type": "string"
        #}}
    #Text: """ + user_input,
    #config={"response_mime_type": "application/json"})
    #data = json.loads(response.text)

        #hotel_name = int(data["hotel_name"])
#hotel_name = "Hey, i'd like to register with your hotel management system. We're called Koala Hotels and have 3 different types of Rooms: Large, Medium, Small"
hotel_name = "koala hotels"
