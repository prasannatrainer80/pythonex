import numpy as np
from sklearn.linear_model import LinearRegression

# Training data
X = np.array([[10], [15], [20], [30], [45]])
y = np.array([2000000, 2800000, 3500000, 4400000, 5700000])

# Create model
model = LinearRegression()

# Train model
model.fit(X, y)

# Predict price for 2200 sq.ft
prediction = model.predict([[42]])

print("Predicted Price:", prediction[0])