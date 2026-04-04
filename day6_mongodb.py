from pymongo import MongoClient
client = MongoClient('mongodb://localhost:27017/')
db = client['mydatabase'] 
users_collection = db['users']
# users_collection.insert_one({"name": "Tom", "age": 40})
# users_collection.insert_one({"name": "Jerry", "age": 20})
# users_collection.insert_one({"name": "Cat", "age": 10})
for user in users_collection.find():
    print(user)

db = client['school_database']

def insert_student(name, age, grade):
    students_collection = db['students']
    student_data = {
        "name": name,
        "age": age,
        "grade": grade
    }
    result = students_collection.insert_one(student_data)
    print(f"Inserted student with ID: {result.inserted_id}")        
def get_students_by_grade(grade):
    students_collection = db['students']
    students = students_collection.find({"grade": grade})
    return list(students)   
def update_student_grade(name, new_grade):
    students_collection = db['students']
    result = students_collection.update_one({"name": name}, {"$set": {"grade": new_grade}})
    if result.modified_count > 0:
        print(f"Updated grade for {name} to {new_grade}")
    else:
        print(f"No student found with name {name}")     
def delete_student(name):
    students_collection = db['students']
    result = students_collection.delete_one({"name": name})
    if result.deleted_count > 0:
        print(f"Deleted student with name {name}")
    else:
        print(f"No student found with name {name}") 
def get_all_students():
    students_collection = db['students']
    students = students_collection.find()
    return list(students)           
if __name__ == "__main__":
    insert_student("Alice", 15, "10th Grade")
    insert_student("Bob", 16, "11th Grade")
    insert_student("Charlie", 14, "9th Grade")
    print("Students in 10th Grade:")
    students_in_10th = get_students_by_grade("10th Grade")
    for student in students_in_10th:
        print(student)
    update_student_grade("Alice", "11th Grade")
    delete_student("Charlie")  
    print('#######################################')
    print("All Students:")  
    for student in get_all_students():
        print(student) 

