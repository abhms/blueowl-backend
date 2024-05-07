from fastapi import APIRouter
from pydantic import BaseModel

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

    item_dict = item.dict()

    response = {
        "message": "Item created successfully",
        "item": item_dict
    }
    
    return response
