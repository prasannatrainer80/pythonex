import mysql.connector

con = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="crt"
)

cur = con.cursor()
print("Connected")
empno=int(input("Enter empno  :    "))
cur.execute("select * from Employ where empno = %s",(empno,))

row = cur.fetchone()
if row:
    print("Employee No   ", row[0])
    print("Employee Name", row[1])
    print("Employee Department ", row[2])
    print("Employee Designation ", row[3])
    print("Employee Salary ", row[4])
else:
    print("Employee No   ", empno, " Not Found")

con.close()