from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from database import connect_to_database
import stripe
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv
import os

app = FastAPI(debug=True)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # You can replace "*" with your frontend domain
    allow_credentials=True,
    allow_methods=["GET", "POST", "PUT", "DELETE"],
    allow_headers=["*"],
)
router = APIRouter()

# Initialize Stripe with your secret key
stripe.api_key = os.getenv("Stripe_secret_key")

class Item(BaseModel):
    name: str
    description: str = None
    price: float
    tax: float = None
    email: str
    mobileNo: str
    address: str


class Payment(BaseModel):
    payment_amount: float

@router.post("/items/")
async def create_item(item: Item):

    # Your existing code to insert data into the database
    connection = connect_to_database()
    cursor = connection.cursor()
    cursor.execute("""
        INSERT INTO patient (name, description, price, email, mobileNo, address)
        VALUES (%s, %s, %s, %s, %s, %s)
    """, (item.name, item.description, item.price, item.email, item.mobileNo, item.address))
    connection.commit()
    cursor.close()
    connection.close()

    item_dict = item.dict()

    response = {
        "message": "Item created successfully",
        "item": item_dict
    }

    return response

@router.post("/payment/")
async def make_payment(payment_amount: Payment):

    try:
        print("Payment Amount:", payment_amount.payment_amount)  # Debugging
        # Create a charge using Stripe
        session = stripe.checkout.Session.create(
            line_items=[{
                'price_data': {
                    'currency': 'usd',
                    'product_data': {
                        'name': 'T-shirt',
                    },
                    'unit_amount': int(payment_amount.payment_amount * 100),  # Convert to cents
                },
                'quantity': 1,
            }],
            mode='payment',
            success_url='http://localhost:4242/success',
            cancel_url='http://localhost:4242/cancel',
        )
    except stripe.error.CardError as e:
        # Error handling
        pass  # Placeholder, replace with actual error handling
    except stripe.error.RateLimitError as e:
        # Error handling
        pass  # Placeholder, replace with actual error handling
    except stripe.error.InvalidRequestError as e:
        # Error handling
        pass  # Placeholder, replace with actual error handling
    except stripe.error.AuthenticationError as e:
        # Error handling
        pass  # Placeholder, replace with actual error handling
    except stripe.error.APIConnectionError as e:
        # Error handling
        pass  # Placeholder, replace with actual error handling
    except stripe.error.StripeError as e:
        # Error handling
        pass  # Placeholder, replace with actual error handling
    except Exception as e:
        # Error handling
        pass  # Placeholder, replace with actual error handling

    # Payment successful
    return {"message": "Payment successful", "session": session}

app.include_router(router)
