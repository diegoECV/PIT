import os
from pymongo import MongoClient
from dotenv import load_dotenv

load_dotenv()

def get_mongodb_connection():
    uri = os.getenv("MONGO_URI")
    client = MongoClient(uri)
    db_name = os.getenv("MONGO_DATABASE")
    return client[db_name]
