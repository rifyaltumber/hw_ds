import mysql.connector

db = mysql.connector.connect(
  host="localhost",
  user=input('user = '),
  password=input('password = ')
)

cursor = db.cursor()
cursor.execute("CREATE DATABASE Aplikasi_Database_Python")

print("Database berhasil dibuat!")