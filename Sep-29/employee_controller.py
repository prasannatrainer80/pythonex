from flask import Blueprint, request, jsonify

from service.employee_service import EmployeeService


employee_controller = Blueprint(
    "employee_controller",
    __name__
)


# ==========================================
# CREATE EMPLOYEE
# POST /api/employees
# ==========================================

@employee_controller.route(
    "/api/employees",
    methods=["POST"]
)
def create_employee():

    data = request.get_json()

    if not data:

        return jsonify({
            "message": "Request body is required"
        }), 400

    required_fields = [
        "empno",
        "name"
    ]

    for field in required_fields:

        if field not in data:

            return jsonify({
                "message": f"{field} is required"
            }), 400

    employee = EmployeeService.create_employee(
        data
    )

    return jsonify({
        "message": "Employee created successfully",
        "employee": employee.to_dict()
    }), 201


# ==========================================
# GET ALL EMPLOYEES
# GET /api/employees
# ==========================================

@employee_controller.route(
    "/api/employees",
    methods=["GET"]
)
def get_all_employees():

    employees = (
        EmployeeService.get_all_employees()
    )

    result = [
        employee.to_dict()
        for employee in employees
    ]

    return jsonify(result), 200


# ==========================================
# GET EMPLOYEE BY ID
# GET /api/employees/<empno>
# ==========================================

@employee_controller.route(
    "/api/employees/<int:empno>",
    methods=["GET"]
)
def get_employee(empno):

    employee = (
        EmployeeService.get_employee_by_id(
            empno
        )
    )

    if employee is None:

        return jsonify({
            "message": "Employee not found"
        }), 404

    return jsonify(
        employee.to_dict()
    ), 200


# ==========================================
# UPDATE EMPLOYEE
# PUT /api/employees/<empno>
# ==========================================

@employee_controller.route(
    "/api/employees/<int:empno>",
    methods=["PUT"]
)
def update_employee(empno):

    data = request.get_json()

    if not data:

        return jsonify({
            "message": "Request body is required"
        }), 400

    employee = EmployeeService.update_employee(
        empno,
        data
    )

    if employee is None:

        return jsonify({
            "message": "Employee not found"
        }), 404

    return jsonify({
        "message": "Employee updated successfully",
        "employee": employee.to_dict()
    }), 200


# ==========================================
# DELETE EMPLOYEE
# DELETE /api/employees/<empno>
# ==========================================

@employee_controller.route(
    "/api/employees/<int:empno>",
    methods=["DELETE"]
)
def delete_employee(empno):

    result = EmployeeService.delete_employee(
        empno
    )

    if not result:

        return jsonify({
            "message": "Employee not found"
        }), 404

    return jsonify({
        "message": "Employee deleted successfully"
    }), 200