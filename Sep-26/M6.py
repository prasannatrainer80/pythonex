from sklearn.tree import DecisionTreeClassifier

X = [
    [2, 12000],
    [3, 15000],
    [4, 20000],
    [5, 30000],
    [6, 50000],
    [7, 90000]
]

# 0 = Fail, 1 = Pass
y = [0, 0, 0, 1, 1, 1]

model = DecisionTreeClassifier()

model.fit(X, y)

result = model.predict([[5, 70000]])

if result[0] == 1:
    print("Pass")
else:
    print("Fail")