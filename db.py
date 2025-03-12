import pymongo
from bson.objectid import ObjectId
import datetime
import os
from dotenv import load_dotenv
load_dotenv()

URI = os.environ.get("MONGO_URI")
NAME = os.environ.get("MONGO_DBNAME")

connection = pymongo.MongoClient(URI)

db = connection[NAME]

"""
user = {
    username: String,
    email: String,
    password: String
}

recipes = {
    name: String,
    description: String,
    steps: List<String>,
    ingredients: List<Ingredients>,
    created_by: UUID (User ID)
    created at: Datetime
}


"""

