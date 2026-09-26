import pandas as pd
from sklearn.linear_model import LinearRegression

data = {
    "amount": [1000000,1000000,1000000,1000000,1000000,1000000,1000000,1000000],
    "period": [1, 2, 3, 4, 5, 6, 7, 8],
    "takehome": [1100000, 1350000, 1500000, 1650000, 1900000, 2200000, 2800000, 4000000]
}

df = pd.DataFrame(data)

X = df[["amount", "period"]]
y = df["takehome"]

model = LinearRegression()
model.fit(X, y)

calculated_amount = model.predict([[1000000, 7.5]])

print("Predicted Marks:", calculated_amount[0])