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
    db_name = "blueowl"

    # Establish connection to MySQL server without selecting a database
    connection = mysql.connector.connect(
        host=db_host,
        user=db_user,
        password=db_password
    )

    # Check if the database exists
    cursor = connection.cursor()
    cursor.execute("SHOW DATABASES")
    databases = [database[0] for database in cursor.fetchall()]
    if db_name not in databases:
        # If the database does not exist, create it
        cursor.execute(f"CREATE DATABASE {db_name}")
        print(f"Database '{db_name}' created successfully")

    # Close cursor as we don't need it anymore
    cursor.close()

    # Connect to the created or existing database
    connection.database = db_name

    # Print message when connection is established
    if connection.is_connected():
        db_info = connection.get_server_info()
        print(f"Connected to MySQL database '{db_name}' (Server version: {db_info})")

    # Create patient table if it doesn't exist
    create_patient_table(connection)

    return connection

def create_patient_table(connection):
    # Define the SQL query to create the patient table
    create_table_query = """
    CREATE TABLE IF NOT EXISTS patient (
        id INT AUTO_INCREMENT PRIMARY KEY,
        name VARCHAR(255) NOT NULL,
        description TEXT,
        price FLOAT NOT NULL,
        email VARCHAR(255) NOT NULL,
        mobileNo VARCHAR(15) NOT NULL,
        address TEXT
    )
    """

    # Execute the SQL query
    cursor = connection.cursor()
    cursor.execute(create_table_query)
    connection.commit()

    # Close cursor as we don't need it anymore
    cursor.close()

    print("Patient table created successfully")

# Example usage
if __name__ == "__main__":
    connect_to_database()
