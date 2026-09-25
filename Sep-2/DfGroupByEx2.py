import pandas as pd
import numpy as np

data={'Category':["Electronics","Furniture","Grocesary","Electronics","Grocesary",
                    "Electronics","Furniture","Grocesary","Electronics","Grocesary",
                  "Electronics","Grocesary","Furniture"
                  ], 'Sales':[665,235,666,255,244,777,872,873,889,566,877,256,356]}
dataFrame=pd.DataFrame(data)
result1=dataFrame.groupby('Category')["Sales"].sum()
print(result1)
result2=dataFrame.groupby('Category')["Sales"].count()
print(result2)
result5=dataFrame.groupby('Category')["Sales"].mean()
print(result5)

result3=dataFrame.groupby('Category')["Sales"].max()
print(result3)
result4=dataFrame.groupby('Category')["Sales"].min()
print(result4)