from flask import jsonify, request

employees = [
    { "id": 1, "name": "Lutfi", "email": "lutfi@email.com", "phone_number": "123-456", "role": "Fighter" },
    { "id": 2, "name": "Joro", "email": "joro@email.com", "phone_number": "090-765", "role": "Jungler" },
    { "id": 3, "name": "Usup", "email": "usup@email.com", "phone_number": "789-567", "role": "Marksman" },
    { "id": 4, "name": "Robun", "email": "robun@email.com", "phone_number": "198-789", "role": "Mage" },
    { "id": 5, "name": "Asri", "email": "asri@email.com", "phone_number": "091-890", "role": "Support" },
]

# Get all employees
def get_all_employees():
    return jsonify({"employees": employees})

# Get employee by ID
def get_employee_by_id(employee_id):
    employee = next((employee for employee in employees if employee["id"] == employee_id), None)
    if employee:
        return jsonify(employee)
    else:
        return jsonify({"error": "Employee not found"}), 404


def add_employee():
    employee_data = request.get_json()    
    employee_id = len(employees) + 1
    employee_data["id"] = employee_id
    employees.append(employee_data)
    
    return jsonify({"id": employee_id, "employee": employee_data}), 201

def update_employee(employee_id):
    employee = next((employee for employee in employees if employee["id"] == employee_id), None)
    if employee:
        updated_data = request.get_json()
        employee.update(updated_data)
        return jsonify(employee)
    else:
        return jsonify({"error": "Employee not found"}), 404


def delete_employee(employee_id):
    global employees
    employee = next((employee for employee in employees if employee["id"] == employee_id), None)
    if employee:
        employees = [a for a in employees if a["id"] != employee_id]
        return jsonify({"message": "Employee deleted"})
    else:
        return jsonify({"error": "Employee not found"}), 404
