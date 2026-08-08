import pandas as pd
import numpy as np
df = pd.read_csv("d:/csv/Data.csv")
print(df)
print("-------------------------------------------------")
table1=pd.pivot_table(df,index=['Name','Qualification'])
# print(table1)
table2=pd.pivot_table(df, values='Name',
    index=['Qualification','Age'],
                      columns=['Qualification'],aggfunc=np.sum)
print(table2)