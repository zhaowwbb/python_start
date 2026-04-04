from fastapi import FastAPI
from pydantic import BaseModel
import sqlite3

#python -m pip install fastapi uvicorn
#python -m uvicorn day6_rest:app --reload
#http://127.0.0.1:8000/docs#/default/get_root__get

class User(BaseModel):
    name: str
    age: int        

def get_db_connection():
    connection = sqlite3.connect('example.db')
    connection.row_factory = sqlite3.Row
    return connection

app = FastAPI()

@app.get("/")
def get_root():
    return {"message": "Hello World"}    

@app.get("/users/")
def get_users_from_db():
    connection = get_db_connection()
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM users")
    users = cursor.fetchall()
    connection.close()
    return users

@app.get("/users/{user_id}")
def read_user(user_id: int):
    connection = get_db_connection()
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM users WHERE id = ?", (user_id,))
    user = cursor.fetchone()
    connection.close()
    return {"user": dict(user) if user else None}

@app.get("/users/search/")          
def find_user_by_name(name: str):
    connection = get_db_connection()
    cursor = connection.cursor()
    formatted_name = f"%{name}%"
    cursor.execute("SELECT * FROM users WHERE name LIKE ?", (formatted_name,))
    users = cursor.fetchall()
    connection.close()
    return users

@app.post("/users/")
def create_user(name: str, age: int):
    connection = get_db_connection()
    cursor = connection.cursor()
    cursor.execute("INSERT INTO users (name, age) VALUES (?, ?)", (name, age))
    connection.commit()
    user_id = cursor.lastrowid
    connection.close()
    return {"user_id": user_id, "name": name, "age": age}       

