import mysql.connector

db = mysql.connector.connect(
  host="localhost",
  user=input('user = '),
  password=input('password = '),
  database="Aplikasi_Database_Python"
)

cursor = db.cursor()
sql = "INSERT INTO customers (name, address) VALUES (%s, %s)"
val = ("Dian", "Mataram")
cursor.execute(sql, val)

db.commit()

print("{} data ditambahkan".format(cursor.rowcount))