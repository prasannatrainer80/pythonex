import mysql.connector
import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

# --------------------------------
# 1. Connect to MySQL
# --------------------------------

connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="ml_demo"
)

print("MySQL connected successfully")


# --------------------------------
# 2. Read data from MySQL
# --------------------------------

query = """
SELECT experience, salary
FROM employee_salary
"""

df = pd.read_sql(query, connection)

print("\nData from MySQL:")
print(df)


# --------------------------------
# 3. Separate X and y
# --------------------------------

X = df[["experience"]]
y = df["salary"]


# --------------------------------
# 4. Split training and testing data
# --------------------------------

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    # test_size=0.2,
    # random_state=42
)


# --------------------------------
# 5. Create Linear Regression model
# --------------------------------

model = LinearRegression()

#
# --------------------------------
# 6. Train the model
# --------------------------------

model.fit(X_train, y_train)

print("\nModel trained successfully")


# --------------------------------
# 7. Test prediction
# --------------------------------

# y_pred = model.predict(X_test)
#
# print("\nActual values:")
# print(y_test.values)
#
# print("\nPredicted values:")
# print(y_pred)


# --------------------------------
# 8. Evaluate model
# --------------------------------
#
# mae = mean_absolute_error(y_test, y_pred)
#
# mse = mean_squared_error(y_test, y_pred)
#
# r2 = r2_score(y_test, y_pred)
#
# print("\nModel Evaluation")
# print("----------------")
# print("MAE :", mae)
# print("MSE :", mse)
# print("R2  :", r2)


# --------------------------------
# 9. Predict salary
# --------------------------------

exp = float(input("Enter Experience (1 to 10 years) "))
experience = [[exp]]
prediction = model.predict(experience)


print("\nPredicted salary for ",experience, " years experience:",
      prediction[0])


# --------------------------------
# 10. Close connection
# --------------------------------

connection.close()