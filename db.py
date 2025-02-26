import pymongo
from bson.objectid import ObjectId
import datetime
import os
from dotenv import load_dotenv
load_dotenv()

# USERNAME = os.environ.get("USERNAME")
# PASSWORD = os.environ.get("PASSWORD")
# HOST_NAME = os.environ.get("HOST_NAME")
# PORT = os.environ.get("PORT", 27017)

connection = pymongo.MongoClient("mongodb://localhost:27017")

db = connection["httpeople"]

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

