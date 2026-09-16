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
SELECT Dept, ROUND(AVG(Basic), 2) AS AverageSalary
FROM Employ
GROUP BY Dept
ORDER BY AverageSalary DESC
"""

df_salary = pd.read_sql(query, conn)

print(df_salary)