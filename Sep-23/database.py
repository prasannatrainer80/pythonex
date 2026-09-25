import mysql.connector

def get_connection():
    con = mysql.connector.connect(
        host="localhost",
        user="root",
        password="root",
        database="studentdb"
    )

    return con