from sklearn.tree import DecisionTreeClassifier

X = [
    [2, 50],
    [3, 60],
    [4, 65],
    [5, 75],
    [6, 80],
    [7, 90]
]

# 0 = Fail, 1 = Pass
y = [0, 0, 0, 1, 1, 1]

model = DecisionTreeClassifier()

model.fit(X, y)

result = model.predict([[5, 70]])

if result[0] == 1:
    print("Pass")
else:
    print("Fail")