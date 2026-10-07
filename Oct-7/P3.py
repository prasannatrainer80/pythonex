import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

# Sample customer data
data = {
    "Customer": ["Karthik", "Shiva", "Khan", "Arvind", "Vaishnavi",
                 "Rishikesh", "Suresh", "Akhil", "Bunny", "Gowtham"],
    "AnnualIncome": [20000, 25000, 30000, 35000, 80000,
                     85000, 90000, 95000, 40099, 47885],
    "SpendingScore": [18900, 22500, 30000, 35000, 78080,
                      89005, 90000, 90905, 60889, 69965]
}

df = pd.DataFrame(data)

# Select features
X = df[["AnnualIncome", "SpendingScore"]]

# Create K-Means model
kmeans = KMeans(n_clusters=3, random_state=30, n_init=10)

# Train model
df["Cluster"] = kmeans.fit_predict(X)

print(df)

# Display cluster centers
print("\nCluster Centers:")
print(kmeans.cluster_centers_)

# Visualization
plt.scatter(
    df["AnnualIncome"],
    df["SpendingScore"],
    c=df["Cluster"]
)

plt.scatter(
    kmeans.cluster_centers_[:, 0],
    kmeans.cluster_centers_[:, 1],
    marker="X",
    s=200
)

plt.xlabel("Annual Income")
plt.ylabel("Spending Score")
plt.title("Customer Segmentation using K-Means")
plt.show()