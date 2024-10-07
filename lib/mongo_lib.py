# library file mongo connection
from pymongo import MongoClient
import os
from dotenv import load_dotenv

load_dotenv()

# Extract the database configuration from env
username = os.getenv("user")
password = os.getenv("password")
host = os.getenv("host")


def database_connection():
    # Construct the MongoDB URI
    mongo_con_uri = f"mongodb+srv://{username}:{password}@{host}"
    # Connect to MongoDB
    conn_client = MongoClient(mongo_con_uri)
    return conn_client
