import database

def query(db, customer_id: int):
    return db.query(database.Hotel).filter(database.Hotel.customerID == customer_id).first()