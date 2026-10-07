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

X = df[["AnnualIncome", "SpendingScore"]]

inertia = []

for k in range(1, 7):

    model = KMeans(
        n_clusters=k,
        random_state=42,
        n_init=10
    )

    model.fit(X)

    inertia.append(model.inertia_)

plt.plot(range(1, 7), inertia, marker="o")

plt.xlabel("Number of Clusters (K)")
plt.ylabel("Inertia")
plt.title("Elbow Method")

plt.show()