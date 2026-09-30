import mysql.connector
import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score

# Connect to MySQL
connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="ml_demo"
)

# Read MySQL data
query = """
SELECT area, bedrooms, age, price
FROM house_price
"""

df = pd.read_sql(query, connection)

print(df)


# Features
X = df[["area", "bedrooms", "age"]]

# Target
y = df["price"]


# Train/Test split
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
)


# Create model
model = LinearRegression()

# Train
model.fit(X_train, y_train)

sqft=int(input("Enter Square Feet size  "))
br=int(input("Enter Bedrooms  "))
yr=int(input("Enter Years   "))

# New house
new_house = [[sqft, br, yr]]

prediction = model.predict(new_house)

print("\nPredicted House Price:")
print(prediction[0])


connection.close()