import pandas as pd
from sklearn.linear_model import LogisticRegression

data = {
    "Age": [22, 25, 28, 30, 35, 40, 45, 50, 26, 32],
    "Salary": [25000, 28000, 32000, 35000, 45000,
               55000, 65000, 70000, 30000, 40000],
    "Experience": [1, 2, 3, 5, 8, 12, 15, 20, 3, 7],
    "LeftCompany": [1, 1, 1, 0, 0, 0, 0, 0, 1, 0]
}

df = pd.DataFrame(data)

X = df[["Age", "Salary", "Experience"]]
y = df["LeftCompany"]

model = LogisticRegression()

model.fit(X, y)

# Employee prediction
employee = [[27, 30000, 3]]

prediction = model.predict(employee)
probability = model.predict_proba(employee)

print("Will Leave:", prediction[0])
print("Probability:", probability[0])