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

# Read employee data
query = "SELECT * FROM Employ"

df = pd.read_sql(query, conn)

print(df)

conn.close()