from fastapi import FastAPI
from database import connect_to_database

app = FastAPI()

# Establish database connection when the application starts
connection = connect_to_database()


@app.get("/")
async def root():
    return {"message": "Hello World"}
