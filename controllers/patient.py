from fastapi import APIRouter
from pydantic import BaseModel
from database import connect_to_database

router = APIRouter()

class Item(BaseModel):
    name: str
    description: str = None
    price: float
    tax: float = None
    email: str
    mobileNo: str
    address: str

@router.post("/items/")
async def create_item(item: Item):

    # Establish connection to the database
    connection = connect_to_database()
    cursor = connection.cursor()

    # Insert data into the Patient table
    cursor.execute("""
        INSERT INTO patient (name, description, price, email, mobileNo, address)
        VALUES (%s, %s, %s, %s, %s, %s)
    """, (item.name, item.description, item.price, item.email, item.mobileNo, item.address))

    # Commit changes to the database
    connection.commit()

    # Close cursor and connection
    cursor.close()
    connection.close()

    # Prepare response
    item_dict = item.dict()
    response = {
        "message": "Item created successfully",
        "item": item_dict
    }

    return response
