from flask import Blueprint
from views.employee import get_all_employees, get_employee_by_id, add_employee, update_employee, delete_employee

employee_bp = Blueprint('employee_bp', __name__)

@employee_bp.route('/employees', methods=['GET'])
def route_get_employees():
    return get_all_employees()

@employee_bp.route('/employees/<int:employee_id>', methods=['GET'])
def route_get_employee(employee_id):
    return get_employee_by_id(employee_id)

@employee_bp.route('/employees', methods=['POST'])
def route_add_employee():
    return add_employee()

@employee_bp.route('/employees/<int:employee_id>', methods=['PUT'])
def route_update_employee(employee_id):
    return update_employee(employee_id)

@employee_bp.route('/employees/<int:employee_id>', methods=['DELETE'])
def route_delete_employee(employee_id):
    return delete_employee(employee_id)
