import pandas as pd
import numpy as np

class Employ:
    def __init__(self,empno, name, salary):
        self.empno = empno
        self.name = name
        self.salary = salary

    def __str__(self):
        return f"Employ No {self.empno}  Employ Name {self.name}  Salary {self.salary}"

e1=Employ(1, "Sindhu", 88233)
e2=Employ(2,"Arjit",88222)
e3=Employ(3,"Yashpal",88999)

empList=[e1, e2, e3]
info=np.array(empList)
pan1=pd.Series(info)
print(pan1)