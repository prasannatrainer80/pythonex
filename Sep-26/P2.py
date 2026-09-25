import pandas as pd

data = {
    "StudyHours": [2, 4, 6, 8, 10],
    "Attendance": [60, 70, 80, 90, 95],
    "Marks": [45, 55, 68, 82, 92]
}

df = pd.DataFrame(data)

print(df)

print(df.head())

print(df.info())

print(df.describe())


print(df.isnull().sum())


print(df.corr())
