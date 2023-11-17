import pymongo
from datetime import datetime

# Connect to MongoDB
client = pymongo.MongoClient("mongodb://localhost:27017/")
database = client["studentData"]  
collection = database["students"]  

# CRUD Operations

# Create (Insert)
def create_student(name, matric_number, dob):
    student_data = {
        "name": name,
        "matric_number": matric_number,
        "dob": dob
    }
    result = collection.insert_one(student_data)
    print(f"Student inserted with ID: {result.inserted_id}")

# Read (Query)
def get_students():
    students = collection.find()
    for student in students:
        print(student)

# Update
def update_student(matric_number, new_name):
    query = {"matric_number": matric_number}
    update_data = {"$set": {"name": new_name}}
    result = collection.update_one(query, update_data)
    print(f"Matched {result.matched_count} document and modified {result.modified_count} document")

# Delete
def delete_student(matric_number):
    query = {"matric_number": matric_number}
    result = collection.delete_one(query)
    print(f"Deleted {result.deleted_count} document")

# Example Usage
create_student("Michael Omaruaye", "20CJ027480", datetime(2004, 9, 4))
create_student("Oluwamuyiwa Tehingbola", "20CJ027491", datetime(2003, 9, 16))
get_students()

update_student("20CJ027480", "Michael Omaruaye Oghenevwona")
get_students()

delete_student("20CJ027491")
get_students()
