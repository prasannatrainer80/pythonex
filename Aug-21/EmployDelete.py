import mysql.connector

con = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="crt"
)

cur = con.cursor()
print("Connected")
empno=int(input("Enter empno: "))
sql="delete from Employ where empno = %s"
cur.execute(sql,(empno,))
con.commit()
print("Deleted successfully")
cur.close()