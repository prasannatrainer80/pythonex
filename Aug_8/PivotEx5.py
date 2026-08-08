import pandas as pd
import numpy as np

df = pd.read_csv("d:/csv/Data_Dup.csv")
print(df)
duplicates=df[df.duplicated()]
print("Result after duplicates")
print(duplicates)