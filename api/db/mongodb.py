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

def get_agents_collection():
    return get_db()["agents"]

def get_flows_collection():
    return get_db()["flows"]

def get_plans_collection():
    return get_db()["plans"]

def get_graphs_collection():
    return get_db()["graphs"]

def get_chats_collection():
    return get_db()["chats"]

def get_messages_collection():
    return get_db()["messages"]
