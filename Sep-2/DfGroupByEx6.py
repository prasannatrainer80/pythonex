import numpy as np
import pandas as pd

df = pd.read_csv("https://media.geeksforgeeks.org/wp-content/uploads/nba.csv")

result_data=df.groupby(["Team","Position"]).agg(
    total_salary=('Salary','sum'),
    avg_salary=('Salary','mean'),
    player_count=('Salary','count'),
    max_salary=('Salary','max'),
    min_salary=('Salary','min')
)
print(result_data)