import numpy as np
from sklearn.linear_model import LinearRegression

# Training data
X = np.array([[1000], [1500], [2000], [2500], [3000]])
y = np.array([2000000, 3000000, 4000000, 5000000, 6000000])

# Create model
model = LinearRegression()

# Train model
model.fit(X, y)

# Predict price for 2200 sq.ft
prediction = model.predict([[2200]])

print("Predicted Price:", prediction[0])