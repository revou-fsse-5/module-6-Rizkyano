from flask import Blueprint, jsonify, request

animals=[
    { "id":1,"species": "Lion", "age": 5, "gender": "Male"},
    { "id":2,"species": "Monkey", "age": 2, "gender": "Male"},
    { "id":3,"species": "Zebra", "age": 1, "gender": "Male"},
    { "id":4,"species": "Tiger", "age": 4, "gender": "Male"},
    { "id":5,"species": "Giraffe", "age": 3, "gender": "Male"}
]

def get_all_animals():
    return jsonify({"animals": animals})

def get_animal_by_id(animal_id):
    animal = next((animal for animal in animals if animal["id"] == animal_id), None)
    if animal:
        return jsonify(animal)
    else:
        return jsonify({"error": "Animal not found"}), 404


def add_animal():
    animal_data = request.get_json()
    animal_id = len(animals) + 1
    animal_data["id"] = animal_id
    animals.append(animal_data)
    return jsonify({"id": animal_id, "animal": animal_data}), 201


def update_animal(animal_id):
    animal = next((animal for animal in animals if animal["id"] == animal_id), None)
    if animal:
        updated_data = request.get_json()
        animal.update(updated_data)
        return jsonify(animal)
    else:
        return jsonify({"error": "Animal not found"}), 404


def delete_animal(animal_id):
    global animals
    animal = next((animal for animal in animals if animal["id"] == animal_id), None)
    if animal:
        animals = [a for a in animals if a["id"] != animal_id]
        return jsonify({"message": "Animal deleted"})
    else:
        return jsonify({"error": "Animal not found"}), 404