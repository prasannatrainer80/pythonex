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

df_dept = pd.read_sql(query, conn)

print(df_dept)