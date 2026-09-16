import mysql.connector
import pandas as pd
import matplotlib.pyplot as plt

# Connect to MySQL
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="crt"
)

print("MySQL Connected Successfully")
query = """
SELECT Dept, COUNT(*) AS EmployeeCount
FROM Employ
GROUP BY Dept
"""

df = pd.read_sql(query, conn)

plt.figure(figsize=(8, 5))

plt.bar(df["Dept"], df["EmployeeCount"])

plt.title("Department-wise Employee Count")
plt.xlabel("Department")
plt.ylabel("Number of Employees")

plt.show()

conn.close()