# database.py

from dotenv import load_dotenv
import mysql.connector
import os

# Load environment variables from .env file
load_dotenv()

def connect_to_database():
    # Retrieve database credentials from environment variables
    db_host = os.getenv("DB_HOST")
    db_user = os.getenv("DB_USERNAME")
    db_password = os.getenv("DB_PASSWORD")
    db_name = os.getenv("DATABASE")

    # Establish connection
    connection = mysql.connector.connect(
        host=db_host,
        user=db_user,
        password=db_password,
        database=db_name
    )

    # Print message when connection is established
    if connection.is_connected():
        db_info = connection.get_server_info()
        print(f"Connected to MySQL database (Server version: {db_info})")

    return connection
