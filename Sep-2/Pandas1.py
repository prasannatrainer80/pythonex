import pandas
import pandas as pd
import numpy as np
names=np.array(["Bala","Jashwanthi","Yashpal","Utkarsh","Sindhu"])
# convert numpy into panda series
ser = pandas.Series(names)
print(ser)