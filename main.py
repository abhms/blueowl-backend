from fastapi import FastAPI
from database import connect_to_database
from controllers.patient import router as item_router

app = FastAPI()

# Establish database connection when the application starts
connection = connect_to_database()

# Include the item router
app.include_router(item_router)

@app.get("/")
async def root():
    return {"message": "Hello World"}
