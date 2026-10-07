import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

data = {
    "StudyHours": [1, 2, 2, 3, 8, 9, 10, 11],
    "Marks":      [35, 40, 45, 50, 75, 80, 85, 90]
}

df = pd.DataFrame(data)

print(df)

# Create K-Means model
model = KMeans(n_clusters=2)

# Train model
model.fit(df)

# Add cluster number
df["Cluster"] = model.labels_

print(df)

# Plot clusters
plt.scatter(
    df["StudyHours"],
    df["Marks"],
    c=df["Cluster"]
)

plt.xlabel("Study Hours")
plt.ylabel("Marks")
plt.title("Student Clustering")

plt.show()