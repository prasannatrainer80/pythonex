class Employ:
    def __int__(self,employee_id,employee_name,employee_city,employee_salary):
        self.employee_id=employee_id
        self.employee_name=employee_name
        self.employee_city=employee_city
        self.employee_salary=employee_salary

class Deba(Employ):
    def __init__(self,employee_id,employee_name,employee_city,employee_salary):
        super().__int__()