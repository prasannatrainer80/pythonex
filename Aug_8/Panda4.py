import pandas as pd
import numpy as np

x=pd.Series("JBIT",index=[0,1,2,3])
print(x)

x1=pd.Series(data=["Raj","Manoj","Kiran",
                   "Nalini"],index=[1,2,3,4])
print(x1)
print(x1.size)
print("===============================")
x2=pd.Series(["Raj","Manoj","Kiran",
                   "Nalini"])
print(x2)
print(x2.size)