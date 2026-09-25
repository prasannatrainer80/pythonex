import mysql.connector
import pandas as pd
import matplotlib.pyplot as plt

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="crt"
)

query = """
SELECT Dept, AVG(Basic) AS AverageSalary
FROM Employ
GROUP BY Dept
"""

df = pd.read_sql(query, conn)

plt.figure(figsize=(8, 5))

plt.bar(df["Dept"], df["AverageSalary"])

plt.title("Department-wise Average Salary")
plt.xlabel("Department")
plt.ylabel("Average Basic Salary")

plt.show()

conn.close()