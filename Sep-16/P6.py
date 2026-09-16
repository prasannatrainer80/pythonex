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
SELECT Name, Basic
FROM Employ
ORDER BY Basic DESC
"""

df = pd.read_sql(query, conn)

plt.figure(figsize=(10, 5))

plt.bar(df["Name"], df["Basic"])

plt.title("Employee Salary Comparison")
plt.xlabel("Employee Name")
plt.ylabel("Basic Salary")

plt.xticks(rotation=45)

plt.show()

conn.close()