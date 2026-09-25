import numpy as np
import pandas as pd

employData = {"empno": [1,2,3,4,5,6,7,8],"name":["Raj","Sindhu","Manoj","Kalyan","Jashwanthi","Raj","Manoj","Jashwanthi"],
              "department":["Java","Python","Java","Python","Java","Java","Python","Python"],
              "salaries":[52233,22555,88822,42522,99922,99999,88888,78887]
              }
df=pd.DataFrame(employData)
# print(df)
result1=df.groupby(["department","name"])
print(result1.first())