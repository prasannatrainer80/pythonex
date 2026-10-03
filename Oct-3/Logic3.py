import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

data = {
    "Glucose": [85, 90, 110, 120, 130, 150, 160, 180, 200, 220],
    "BMI": [22, 23, 25, 26, 28, 30, 32, 35, 37, 40],
    "Age": [25, 27, 30, 32, 35, 40, 45, 50, 55, 60],
    "Diabetes": [0, 0, 0, 0, 0, 1, 1, 1, 1, 1]
}

df = pd.DataFrame(data)

X = df[["Glucose", "BMI", "Age"]]
y = df["Diabetes"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y
)

model = LogisticRegression()

model.fit(X_train, y_train)

y_pred = model.predict(X_test)

print("Accuracy:", accuracy_score(y_test, y_pred))