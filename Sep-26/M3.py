import pandas as pd
from sklearn.linear_model import LinearRegression

data = {
    "hours": [1, 2, 3, 4, 5, 6, 7, 8],
    "attendance": [60, 65, 70, 75, 80, 85, 90, 95],
    "marks": [35, 40, 50, 55, 65, 70, 80, 90]
}

df = pd.DataFrame(data)

X = df[["hours", "attendance"]]
y = df["marks"]

model = LinearRegression()
model.fit(X, y)

marks = model.predict([[6, 88]])

print("Predicted Marks:", marks[0])