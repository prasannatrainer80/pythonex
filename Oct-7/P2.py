import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

data = {
    "Income": [20000, 25000, 30000, 35000, 80000, 85000, 90000, 95000, 40099, 47885],
    "Spending": [18900, 22500, 30000, 35000, 78080, 89005, 90000, 90905, 60889, 69965]
}

df = pd.DataFrame(data)

model = KMeans(
    n_clusters=3,
    random_state=42,
    n_init=10
)

model.fit(df)

df["Cluster"] = model.labels_

print(df)

plt.scatter(
    df["Income"],
    df["Spending"],
    c=df["Cluster"]
)

plt.xlabel("Annual Income")
plt.ylabel("Spending Score")
plt.title("Customer Segmentation")

plt.show()
