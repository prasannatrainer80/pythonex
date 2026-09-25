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
name=input("Enter name: ")
gender=input("Enter gender (MALE or FEMALE): ")
dept=input("Enter department: ")
desig=input("Enter desig: ")
basic=input("Enter basic: ")
sql=("Insert into Employ(empno,name,gender,dept,desig,basic) "
     "values(%s,%s,%s,%s,%s,%s)")
data = (empno,name,gender,dept,desig,basic)
cur.execute(sql,data)
print("Inserted successfully")
con.commit()
cur.close()
