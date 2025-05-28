import os
from pymongo import MongoClient

def get_db():
    """Connect to MongoDB using environment variables."""
    mongo_uri = os.getenv("MONGODB_URI")
    mongo_db = os.getenv("MONGODB_DATABASE")
    client = MongoClient(mongo_uri)
    return client[mongo_db]

def get_apps_collection():
    return get_db()["apps"]

def get_graphs_collection():
    return get_db()["graphs"]
