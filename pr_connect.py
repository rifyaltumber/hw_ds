import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user=input('user = '),
    password=input('password = ')
)

if db.is_connected():
    print("Bershasil terhubung ke database")