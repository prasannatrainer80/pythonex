class Employ:
    def __init__(self,empno, name, basic):
        self.empno = empno
        self.name = name
        self.basic = basic

    def __str__(self):
        return "Employ No " +str(self.empno) + " Employ Name " +self.name + " Salary " +str(self.basic)

class Debashis(Employ):
    def __init__(self, empno, name, basic):
        super().__init__(empno, name, basic)

class Sindhu(Employ):
    def __init__(self, empno, name, basic):
        super().__init__(empno, name, basic)

class Prashanth(Employ):
    def __init__(self,empno, name, basic):
        super().__init__(empno, name, basic)

debashis=Debashis(1,"Debhasis",88233)
sindhu=Sindhu(3,"Sindhu",88233)
prashanth=Prashanth(4,"Prashanth",88211)
employList=[debashis, sindhu,prashanth]
for employ in employList:
    print(employ)