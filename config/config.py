
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
import os
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())
connection_string = os.getenv("mongo_connection_string")

uri = connection_string

# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'))

# Create Database & collections
db_name = client.BlogApp
blog_collections = db_name["blogsPost"]

# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)