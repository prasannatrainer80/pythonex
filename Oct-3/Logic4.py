import pandas as pd
from sklearn.linear_model import LogisticRegression

data = {
    "Income": [20000, 25000, 30000, 35000, 40000,
               50000, 60000, 70000, 80000, 90000],
    "CreditScore": [550, 580, 600, 620, 650,
                    680, 700, 730, 760, 800],
    "LoanAmount": [500000, 450000, 400000, 350000, 300000,
                   300000, 250000, 250000, 200000, 200000],
    "Approved": [0, 0, 0, 0, 1, 1, 1, 1, 1, 1]
}

df = pd.DataFrame(data)

X = df[["Income", "CreditScore", "LoanAmount"]]
y = df["Approved"]

model = LogisticRegression()

model.fit(X, y)

application = [[55000, 690, 300000]]

prediction = model.predict(application)
probability = model.predict_proba(application)

print("Approved:", prediction[0])
print("Approval Probability:", probability[0][1])