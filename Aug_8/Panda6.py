import pandas as pd
import numpy as np
df = pd.read_csv("d:/csv/Data.csv")
print(df)
table=df.pivot(index=['Qualification'], columns='Name',values='Age')
print(table)
print("----------------------------------------------")
table1=df.pivot(index=['Name'],columns='Age',values='Qualification')
print(table1)
print("------------------------------------------------")
table2=df.pivot(index=['Age'], columns='Name',values='Qualification')
print(table2)