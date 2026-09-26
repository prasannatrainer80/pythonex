import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression

data = {
    "StudyHours": [2, 4, 6, 8, 10],
    "Attendance": [60, 70, 80, 90, 95],
    "Marks": [45, 55, 68, 82, 92]
}

df = pd.DataFrame(data)

# print(df)

X = df[["StudyHours", "Attendance"]]
y = df["Marks"]

model = LinearRegression()
model.fit(X, y)

marks = model.predict([[6, 88]])

print("Predicted Marks:", marks[0])