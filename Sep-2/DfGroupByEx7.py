import numpy as np
import pandas as pd

df = pd.read_csv("https://media.geeksforgeeks.org/wp-content/uploads/nba.csv")

df_first_5=df.head(5)
print("First 5 Records are ")
print(df_first_5)
df_sort_3=df.sort_values('Salary',ascending=False).head(3)
print(df_sort_3)