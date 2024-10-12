import pytest
from flask import Flask
from app import animal_bp 

@pytest.fixture
def app():
    app = Flask(__name__)
    app.register_blueprint(animal_bp)
    
    app.config['TESTING'] = True
    return app

@pytest.fixture
def client(app):
    return app.test_client()

def test_get_all_animals(client):

    response = client.get('/animals')
    assert response.status_code == 200


def test_get_animal_by_id(client):

    response = client.get('/animals/1')
    assert response.status_code == 200

def test_add_animal(client):

    response = client.post('/animals', json={
        'gender': 'Male',
        'species': 'Leo',
        'age': 5
    })
    assert response.status_code == 201


def test_update_animal(client):

    response = client.put('/animals/1', json={
        'species': 'Crocodile',
        'age': 6
    })
    assert response.status_code == 200

def test_delete_animal(client):
    post_response = client.post('/animals', json={
        'species': 'Penguin',
        'age': 3,
        'gender': 'Male',
    })
    animal_id = post_response.json['id']

    delete_response = client.delete(f'/animals/{animal_id}')
    assert delete_response.status_code == 200

    get_response = client.get(f'/animals/{animal_id}')
    assert get_response.status_code == 404