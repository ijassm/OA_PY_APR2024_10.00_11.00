from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from data import *

username = "Enter your username"
password = "Enter your password"

uri = f"mongodb+srv://{username}:{password}@students.jooqal4.mongodb.net/?retryWrites=true&w=majority"

# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi("1"))

# Send a ping to confirm a successful connection
try:
    client.admin.command("ping")
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)


db = client["OA_PY_APRIL_10_11"]

student = db["students"]

# doc = {
#     "firstName": "John",
#     "lastName": "Wick",
#     "mobileNumber": 9876543210,
#     "countryCode": "+91",
#     "age": 10,
#     "skills": ["Assassin", "Shooting", "Fighting"],
#     "address": {
#         "street": "Mariamman st",
#         "city": "Puducherry",
#         "state": "Puducherry",
#         "country": "India",
#     },
# }

# student.insert_one(doc)

# student.insert_many(data)

# GET

# result = list(student.find())

# for i in result:
#     print("FullName : ", i["firstName"] + i["lastName"])
#     print(i, end="\n\n")
