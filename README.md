# BlueOwl

This project, BlueOwl, is built using FastAPI and utilizes a MySQL database to store data. The API is designed to be robust and efficient, suitable for various applications.

## clone
```
git clone https://github.com/abhms/blueowl-backend.git
cd blueowl-backend
```

## Setting Up MySQL
```
mysql -u root -p

CREATE DATABASE blueowl;

```

## Configuring Environment Variables
Create a .env file in the root directory of the project and add the following configuration, replacing values with your actual database settings and API keys:

```
DB_HOST=localhost
DB_USER=user
DB_PASSWORD=password
DB_DATABASE=blueowl
STRIPE_KEY=your_stripe_secret_key
```

## Installing Dependencies

Install the necessary dependencies by running the following command:

```
pip install -r requirements.txt
```

## Running the Application
To run the application, use the following command:
```
uvicorn main:app --reload

```