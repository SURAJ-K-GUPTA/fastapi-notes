from pymongo import MongoClient
from dotenv import load_dotenv
import os
load_dotenv()

# Connect to MongoDB
MONGO_URI = os.getenv("MONGO_URI")
client = MongoClient(MONGO_URI)
notesdb = client.get_database("notes")  # Database
notescollection = notesdb.get_collection("notes") # Collection