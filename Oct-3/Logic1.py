import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report

# Dataset
data = {
    "StudyHours": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    "Attendance": [50, 55, 60, 65, 70, 75, 80, 85, 90, 95],
    "Pass": [0, 0, 0, 0, 1, 1, 1, 1, 1, 1]
}

df = pd.DataFrame(data)

# Input and output
X = df[["StudyHours", "Attendance"]]
y = df["Pass"]

# Split dataset
X_train, X_test, y_train, y_test = train_test_split(
    X, y
)

# Create model
model = LogisticRegression()

# Train
model.fit(X_train, y_train)

# # Prediction
# y_pred = model.predict(X_test)
#
# print("Accuracy:", accuracy_score(y_test, y_pred))
# print(classification_report(y_test, y_pred))

# New student
new_student1 = [[6, 80]]

prediction = model.predict(new_student1)
probability = model.predict_proba(new_student1)

print("Prediction:", prediction)
print("Probability:", probability)

new_student2 = [[2, 40]]

prediction = model.predict(new_student2)
probability = model.predict_proba(new_student2)

print("Prediction:", prediction)
print("Probability:", probability)
