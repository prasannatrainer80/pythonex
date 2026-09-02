import numpy as np
import pandas as pd

df = pd.read_csv("d:/csv/Employs.csv")
result_data=df.groupby("Dept").agg(
    total_salary=('Salary','sum'),
    avg_salary=('Salary','mean'),
    player_count=('Salary','count'),
    max_salary=('Salary','max'),
    min_salary=('Salary','min')
)
print(result_data)

result1=df.groupby("Dept")["Salary"].sum()
print(result1)
result_2=df.groupby("Gender")["Gender"].count()
print(result_2)
result2=df.groupby("Dept")["Salary"].count()
print(result2)
result3=df.groupby("Dept")["Salary"].max()
print("Max Salaries ")
print(result3)
result4=df.groupby("Dept")["Salary"].min()
print("Min Salaries ")
print(result4)

result1=df.head(5)
print(result1)
result3=df.sort_values("Salary",ascending=False)
print(result3)
result2=df.sort_values("Salary",ascending=False).head(1)
print(result2)
result_max_5_sal=df.sort_values("Salary",ascending=False).head(5)
print("First Five Top employes based on Salary-Wise  ")
print(result_max_5_sal)