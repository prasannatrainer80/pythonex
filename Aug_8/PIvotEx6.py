import pandas as pd
import numpy as np
df = pd.read_csv("d:/csv/Employ_Data.csv")
print(df)
print("Sort above data name-wise ")
df.sort_values("Name",inplace=True)
print(df)
print("Sort Above Data salary-wise")
df.sort_values("Salary",inplace=True)
print(df)
