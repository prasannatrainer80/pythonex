import pandas as pd
import numpy as np

info={"Yashpal":88234.22,"Sindhu":88112,"Arjit":88223,"Utkarsh":81134,"Bala":94222}
# convert Dictionary to Panda Series
a=pd.Series(info)
print(a)