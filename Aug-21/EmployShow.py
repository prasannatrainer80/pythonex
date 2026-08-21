import mysql.connector

con = mysql.connector.connect(
    host="localhost",
    user="root",
    # port="3307",
    password="root",
    database="crt"
)

cur = con.cursor()
print("Connected")
cur.execute("select * from Employ")
rows = cur.fetchall()
for row in rows:
    print(row)

con.close()