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
SELECT Gender, COUNT(*) AS EmployeeCount
FROM Employ
GROUP BY Gender
"""

df = pd.read_sql(query, conn)

plt.figure(figsize=(6, 6))

plt.pie(
    df["EmployeeCount"],
    labels=df["Gender"],
    autopct="%1.1f%%"
)

plt.title("Gender-wise Employee Distribution")

plt.show()

conn.close()