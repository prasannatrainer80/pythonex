import pandas as pd
from sklearn.linear_model import LinearRegression

data = {
    "StudyHours": [2, 4, 6, 8, 10],
    "Marks": [45, 55, 68, 82, 92]
}

df = pd.DataFrame(data)

X = df[["StudyHours"]]
y = df["Marks"]

model = LinearRegression()

model.fit(X, y)

prediction = model.predict([[7]])

print("Predicted Marks:", prediction[0])
