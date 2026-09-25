import mysql.connector
import pandas as pd
import matplotlib.pyplot as plt

# --------------------------------
# 1. MySQL Connection
# --------------------------------

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="crt"
)

print("Connected to MySQL")

# --------------------------------
# 2. Department-wise Employee Count
# --------------------------------

query1 = """
SELECT Dept, COUNT(*) AS EmployeeCount
FROM Employ
GROUP BY Dept
"""

df_dept = pd.read_sql(query1, conn)

# --------------------------------
# 3. Department-wise Average Salary
# --------------------------------

query2 = """
SELECT Dept, AVG(Basic) AS AverageSalary
FROM Employ
GROUP BY Dept
"""

df_salary = pd.read_sql(query2, conn)

# --------------------------------
# 4. Employee Salary Comparison
# --------------------------------

query3 = """
SELECT Name, Basic
FROM Employ
ORDER BY Basic DESC
"""

df_employee = pd.read_sql(query3, conn)

# --------------------------------
# 5. Gender-wise Employee Count
# --------------------------------

query4 = """
SELECT Gender, COUNT(*) AS EmployeeCount
FROM Employ
GROUP BY Gender
"""

df_gender = pd.read_sql(query4, conn)

# --------------------------------
# 6. Display Data
# --------------------------------

print("\nDepartment-wise Employee Count")
print(df_dept)

print("\nDepartment-wise Average Salary")
print(df_salary)

print("\nEmployee Salary Comparison")
print(df_employee)

print("\nGender-wise Employee Count")
print(df_gender)

# --------------------------------
# 7. Graph 1: Department Count
# --------------------------------

plt.figure(figsize=(8, 5))

plt.bar(df_dept["Dept"], df_dept["EmployeeCount"])

plt.title("Department-wise Employee Count")
plt.xlabel("Department")
plt.ylabel("Employee Count")

plt.show()

# --------------------------------
# 8. Graph 2: Average Salary
# --------------------------------

plt.figure(figsize=(8, 5))

plt.bar(df_salary["Dept"], df_salary["AverageSalary"])

plt.title("Department-wise Average Salary")
plt.xlabel("Department")
plt.ylabel("Average Salary")

plt.show()

# --------------------------------
# 9. Graph 3: Employee Salary
# --------------------------------

plt.figure(figsize=(10, 5))

plt.bar(df_employee["Name"], df_employee["Basic"])

plt.title("Employee Salary Comparison")
plt.xlabel("Employee Name")
plt.ylabel("Basic Salary")

plt.xticks(rotation=45)

plt.show()

# --------------------------------
# 10. Graph 4: Gender Distribution
# --------------------------------

plt.figure(figsize=(6, 6))

plt.pie(
    df_gender["EmployeeCount"],
    labels=df_gender["Gender"],
    autopct="%1.1f%%"
)

plt.title("Gender-wise Employee Distribution")

plt.show()

# --------------------------------
# 11. Close Connection
# --------------------------------

conn.close()