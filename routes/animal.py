from flask import Blueprint
from views.animal import get_all_animals, get_animal_by_id, add_animal, update_animal, delete_animal

animal_bp = Blueprint('animal_bp', __name__)

@animal_bp.route('/animals', methods=['GET'])
def route_get_animals():
    return get_all_animals()

@animal_bp.route('/animals/<int:animal_id>', methods=['GET'])
def route_get_animal(animal_id):
    return get_animal_by_id(animal_id)

@animal_bp.route('/animals', methods=['POST'])
def route_add_animal():
    return add_animal()

@animal_bp.route('/animals/<int:animal_id>', methods=['PUT'])
def route_update_animal(animal_id):
    return update_animal(animal_id)

@animal_bp.route('/animals/<int:animal_id>', methods=['DELETE'])
def route_delete_animal(animal_id):
    return delete_animal(animal_id)
