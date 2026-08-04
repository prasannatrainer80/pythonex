class Employ:
    def __init__(self, employee_id, employee_name, employee_age, employee_salary):
        self.employee_id = employee_id
        self.employee_name = employee_name
        self.employee_age = employee_age
        self.employee_salary = employee_salary

    def __str__(self):
        return str(self.employee_id) + str(self.employee_name) + str(self.employee_age) + str(self.employee_salary)

class Debashis(Employ):
    def __init__(self, employee_id, employee_name, employee_age, employee_salary):
        super().__init__( employee_id, employee_name, employee_age,employee_salary)

class Sneha(Employ):
    def __init__(self, employee_id, employee_name, employee_age, employee_salary):
        super().__init__(employee_id, employee_name, employee_age,employee_salary)

debashis = Debashis(employee_id=1, employee_name="deba", employee_age=20, employee_salary=100 )
sneha = Sneha(employee_id=2, employee_name="sneha", employee_age=20, employee_salary=100 )
print(debashis)
print(sneha)