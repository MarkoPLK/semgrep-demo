import sqlite3

API_KEY = "AWS-1234567890abcdef"  

user_input = input("Introduce tu nombre: ")
query = "SELECT * FROM users WHERE name = '" + user_input + "'"

conn = sqlite3.connect("database.db")
cursor = conn.cursor()
cursor.execute(query)
