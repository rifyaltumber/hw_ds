import mysql.connector

db = mysql.connector.connect(
  host="localhost",
  user=input('user = '),
  password=input('password = '),
  database="Aplikasi_Database_Python"
)

cursor = db.cursor()
sql = "SELECT * FROM customers"
cursor.execute(sql)

results = cursor.fetchall()

for data in results:
  print(data)