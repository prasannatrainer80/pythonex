import pandas as pd
import numpy as np

x2=pd.Series(data=["Raj","Manoj",
                   "Kiran","Nalini"],
             index=["zero","one","two","three"])
print(x2)
print(x2.index)
print(x2.shape)
print(x2.size)