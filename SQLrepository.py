import database
def query():
    query(database.Hotel).filter(database.Hotel.customerID == database.customerID).first()