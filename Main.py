import database
import CRUD
from fastapi import FastAPI
from CRUD import router

app = FastAPI()

app.include_router(router)

if __name__ == "__main__":
    database.start_db()
    CRUD.start_crud()






    

    


