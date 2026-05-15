import sqlite3

connection = sqlite3.connect('example.db')
cursor = connection.cursor()
cursor.execute('''CREATE TABLE IF NOT EXISTS users
                  (id INTEGER PRIMARY KEY, name TEXT, age INTEGER)''')  
connection.commit()
cursor.execute("INSERT INTO users (name, age) VALUES (?, ?)", ("Tom", 40))
cursor.execute("INSERT INTO users (name, age) VALUES (?, ?)", ("Jerry", 20))
cursor.execute("INSERT INTO users (name, age) VALUES (?, ?)", ("Cat", 10))
connection.commit()
cursor.execute("SELECT * FROM users")
rows = cursor.fetchall()
for row in rows:
    print(row)
connection.close()
