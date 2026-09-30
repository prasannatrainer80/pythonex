import pandas as pd

data = {
    "StudyHours": [1,2,3,4,5,6,7,8,9,10],
    "Attendance": [50,55,60,65,70,75,80,85,90,95],
    "PreviousMarks": [30,35,40,45,50,60,65,70,80,85],
    "Result": [0,0,0,0,1,1,1,1,1,1]
}

df = pd.DataFrame(data)

print(df)
# Train model
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier

X = df[
    [
        "StudyHours",
        "Attendance",
        "PreviousMarks"
    ]
]

y = df["Result"]

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

model = RandomForestClassifier(
    n_estimators=100,
    random_state=42
)

model.fit(X_train, y_train)
# Make prediction
new_student = [[6, 75, 60]]

prediction = model.predict(new_student)

if prediction[0] == 1:
    print("Student is predicted to PASS")
else:
    print("Student is predicted to FAIL")