from fastapi import FastAPI
from database import connect_to_database
from controllers.patient import router as item_router
from fastapi import APIRouter
from fastapi.middleware.cors import CORSMiddleware

# Add CORS middleware to your FastAPI application
app = FastAPI()
router = APIRouter()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # You can replace "*" with your frontend domain
    allow_credentials=True,
    allow_methods=["GET", "POST", "PUT", "DELETE"],
    allow_headers=["*"],
)

# Include the item router
app.include_router(item_router)
@router.get("/getdata/{patient_id}")
async def get_patient_data(patient_id: int):
    # Establish connection to the database
    connection = connect_to_database()
    cursor = connection.cursor()

    # Fetch patient data by ID
    cursor.execute("SELECT * FROM patient WHERE id = %s", (patient_id,))
    patient_data = cursor.fetchone()

    # Close cursor and connection
    cursor.close()
    connection.close()

    # Check if patient data exists
    if patient_data:
        # Prepare response
        response_data = {
            "id": patient_data[0],
            "name": patient_data[1],
            "description": patient_data[2],
            "price": patient_data[3],
            "email": patient_data[4],
            "mobileNo": patient_data[5],
            "address": patient_data[6]
        }
        return response_data
    else:
        return {"message": "Patient not found"}

# Define the root endpoint within the router
@router.get("/")
async def root():
    # Establish connection to the database
    connection = connect_to_database()
    cursor = connection.cursor()

    # Fetch all data from the patient table
    cursor.execute("SELECT * FROM patient")
    patient_data = cursor.fetchall()

    # Close cursor and connection
    cursor.close()
    connection.close()

    # Prepare response
    response_data = [{"id": row[0], "name": row[1], "description": row[2], "price": row[3], "email": row[4], "mobileNo": row[5], "address": row[6]} for row in patient_data]

    return {"patients": response_data}

# Include the router in the FastAPI application
app.include_router(router)
