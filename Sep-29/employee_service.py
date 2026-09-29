from database import db
from model.employee import Employee


class EmployeeService:

    # --------------------------------
    # CREATE
    # --------------------------------
    @staticmethod
    def create_employee(data):

        employee = Employee(
            empno=data["empno"],
            name=data["name"],
            gender=data.get("gender"),
            dept=data.get("dept"),
            desig=data.get("desig"),
            basic=data.get("basic")
        )

        db.session.add(employee)
        db.session.commit()

        return employee

    # --------------------------------
    # GET ALL
    # --------------------------------
    @staticmethod
    def get_all_employees():

        return Employee.query.all()

    # --------------------------------
    # GET BY ID
    # --------------------------------
    @staticmethod
    def get_employee_by_id(empno):

        return db.session.get(Employee, empno)

    # --------------------------------
    # UPDATE
    # --------------------------------
    @staticmethod
    def update_employee(empno, data):

        employee = db.session.get(
            Employee,
            empno
        )

        if employee is None:
            return None

        employee.name = data["name"]
        employee.gender = data.get("gender")
        employee.dept = data.get("dept")
        employee.desig = data.get("desig")
        employee.basic = data.get("basic")

        db.session.commit()

        return employee

    # --------------------------------
    # DELETE
    # --------------------------------
    @staticmethod
    def delete_employee(empno):

        employee = db.session.get(
            Employee,
            empno
        )

        if employee is None:
            return False

        db.session.delete(employee)
        db.session.commit()

        return True