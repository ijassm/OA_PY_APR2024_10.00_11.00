from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from data import *
from bson import ObjectId

username = "ijass"
password = "EdAV0SXSIGWTzPV7"

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

# query = {"age": {"$lt": 30}}
# filter = {
#     "_id": 0,
#     "address": 1,
#     "firstName": 1,
#     "lastName": 1,
# }

# result = list(student.find(query, filter))

# for i in result:
#     print("FullName : ", i["firstName"] + i["lastName"])
#     print(i, end="\n\n")


# update

# query = {"_id": ObjectId("66b9a5d31e31e23c23f452ff")}

# new_values = {"$set": {"age": 20}}

# student.update_one(query, new_values)

# Update all

# query = {"age": 10}

# new_values = {"$set": {"age": 20}}

# student.update_many(query, new_values)


# delete one

# query = {"_id": ObjectId("66b9a907109ef5ca8adc41ef")}

# student.delete_one(query)

# delete all

# query = {}

# student.delete_many(query)

# drop

# student.drop()

# Close the connection

client.close()

print("All operations completed successfully.")

# NOTE: This script assumes that you have a MongoDB Atlas account and have created a cluster, database, and collection. You will need to replace the URI and credentials with your own. If you're using a local MongoDB instance, you can use the MongoClient class provided by pymongo.

# Task

# 1. Create a student
# 2. View all students
# 3. update the student
# 4. update the password


# while True:
#     print("\n1. Create a student")
#     print("2. View all students")
#     print("3. Update the student")
#     print("4. Update the password")
#     print("5. Exit")
#     choice = int(input("Enter your choice: "))

#     if choice == 1:
#         firstName = input("Enter first name: ")
#         lastName = input("Enter last name: ")
#         mobileNumber = int(input("Enter mobile number: "))
#         countryCode = input("Enter country code: ")
#         age = int(input("Enter age: "))
#         skills = input("Enter skills separated by comma: ").split(",")
#         address = {
#             "street": input("Enter street: "),
#             "city": input("Enter city: "),
#             "state": input("Enter state: "),
#             "country": input("Enter country: "),
#         }
