import numpy as np
import pandas as pd

employData = {"empno": [1,2,3,4,5],"name":["Raj","Sindhu","Manoj","Kalyan","Jashwanthi"],
              "department":["Java","Python","Java","Python","Java"],
              "salaries":[52233,22555,88822,42522,99922]
              }
df=pd.DataFrame(employData)
print(employData)

aggregate_data=df.groupby("department").agg(
    total_salary=('salaries','sum'),
    avg_salary=('salaries','mean'),
    total_employs=('salaries','count'),
    max_salary=('salaries','max'),
    min_salary=('salaries','min')
)
print(aggregate_data)

# # group by Department-wise sum
# result1=df.groupby("department")["salaries"].sum()
# print(result1)
# result2=df.groupby("department")["salaries"].count()
# print(result2)
# result3=df.groupby("department")["salaries"].max()
# print("Max Salaries ")
# print(result3)
# result4=df.groupby("department")["salaries"].min()
# print("Min Salaries ")
# print(result4)
