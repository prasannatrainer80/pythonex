class Wipro:
    def __init__(self,empId,empName,empDesig):
        self.empId = empId
        self.empName = empName
        self.empDesig = empDesig

    def __str__(self):
        return ("Employ Id " +str(self.empId) +
                " Employ Name " +self.empName +
                 " Employ Designation " +self.empDesig)

class Java(Wipro):
    def __init__(self,empId,empName,empDesig,salary,workMode):
        # super().__init__(self.empId, self.empName,self.empDesig)
        self.empId = empId
        self.empName = empName
        self.empDesig = empDesig
        self.salary = salary
        self.workMode = workMode

    def __str__(self):
        return ("Employ Id " +str(self.empId) +
                 " Employ Name " +self.empName +
                 " Designation  " +self.empDesig +
                 " Salary  " +str(self.salary) +
                 " WorkMode  " +self.workMode
                )
class Python(Wipro):
    def __init__(self,empId,empName,empDesig,hours,rate,workMode):
        # super().__init__(self.empId, self.empName,self.empDesig)
        self.empId = empId
        self.empName = empName
        self.empDesig = empDesig
        self.hours = hours
        self.rate = rate
        self.workMode = workMode

    def __str__(self):
        takeHome = self.hours * self.rate
        return("Employ Id " +str(self.empId) +
               " Employ Name " +self.empName +
               " Employ Designation " +self.empDesig +
               " Employ Hours  " +str(self.hours) +
               " Rate  " +str(self.rate) +
               " Work Mode " +self.workMode +
               " TakeHome " +str(takeHome))
class Employ:
    def __init__(self,empId,name,wipro):
        self.empId = empId
        self.name = name
        self.wipro = wipro

    def __str__(self):
        return (
            "Employ Id " +str(self.empId) + " Employ Name " +self.name + " JobDetails " +str(self.wipro)
        )

java1=Java(1,"Rajesh","Manager",88822,"Hibrid")
python1=Python(2,"Nalini","Expert",80,5000,"Remote")
java2=Java(3,"Ashok","Director",99999,"Offline")
python2=Python(4,"Debashis","Manager",80,9000,"Offline")

employ1=Employ(1,"Rajshree",java1)
employ2=Employ(2,"Utkarsh",python1)

print(employ1)
print(employ2)