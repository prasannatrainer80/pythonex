class Employ:
    def __init__(self,empId,empName,empDept):
        self.empId = empId
        self.empName = empName
        self.empDept = empDept

    def __str__(self):
        return "Employ Id " +str(self.empId) + " Employ Name " +self.empName + " Department " +str(self.empDept)

class FullTimeEmploy(Employ):
    def __init__(self, empId,empName,empDept,empSalary):
        super().__init__(empId,empName,empDept)
        self.empId = empId
        self.empName=empName
        self.empDept = empDept
        self.empSalary = empSalary

    def __str__(self):
        return ("Employ Id " +str(self.empId) +
                " Employ Name " +self.empName +
                " Department " + self.empDept  +
                " Employ Salary " +str(self.empSalary))

class PartTimeEmploy(Employ):
    def __init__(self,empId,empName,empDept,hours,rate):
        super().__init__(empId,empName,empDept)
        self.empId = empId
        self.empName = empName
        self.empDept = empDept
        self.hours = hours
        self.rate = rate

    def __str__(self):
        takhome = self.hours * self.rate
        return ("Employ Id " + str(self.empId) +
                " Employ Name " + self.empName +
                " Department " + self.empDept +
                " Hours Worked " + str(self.hours) +
                " Billing Rate " +str(self.rate) +
                " Take Home " +str(takhome)
                )

partTimeEmploy=PartTimeEmploy(1, "Prasanna","Python",80,5000)
fullTimeEmploy=FullTimeEmploy(2,"Debashis","Python",80000)
print(partTimeEmploy)
print(fullTimeEmploy)