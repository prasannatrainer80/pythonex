import numpy as np
import pandas as pd

employData = {"empno": [1,2,3,4,5],"name":["Raj","Sindhu","Manoj","Kalyan","Jashwanthi"],
              "department":["Java","Python","Java","Python","Java"],
              "salaries":[52233,22555,88822,42522,99922]
              }
df=pd.DataFrame(employData)
# print(df)
result1=df.groupby("department")
print(result1.first())