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
sql=("update employ set name = %s, gender = %s, dept = %s, desig = %s,"
     " basic = %s where empno = %s")
data = (name,gender,dept,desig,basic,empno)
cur.execute(sql,data)
print("Updated successfully")
con.commit()
cur.close()
