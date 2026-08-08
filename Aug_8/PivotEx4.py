import numpy as np
import pandas as pd
from pandas import pivot

df = pd.read_csv("d:/csv/Employs.csv")
# print(df.head())
print("After Pivot Data is  ")
result=df.pivot(index=['Dept'], columns='name',values='Salary')
print(result.head())

result1=df.pivot(index=['Gender','Desig'],columns='name',values='Salary')
print("Second Pivot Data is  ")
print(result1.head(18))