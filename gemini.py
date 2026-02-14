import os
import json
from dotenv import load_dotenv
from google import genai


load_dotenv()
client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

def ai(user_input):
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
    #return hotelTable_name

