# 🧪 ML LAB 3 — Data Visualization
import matplotlib.pyplot as plt
import pandas as pd

data = {
    "StudyHours": [2, 4, 6, 8, 10],
    "Attendance": [60, 70, 80, 90, 95],
    "Marks": [45, 55, 68, 82, 92]
}

df = pd.DataFrame(data)


plt.bar(df["StudyHours"], df["Marks"])

plt.xlabel("Study Hours")
plt.ylabel("Marks")
plt.title("Study Hours vs Marks")

plt.show()
