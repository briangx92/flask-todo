from flask_todo import create_app


def test_config():
    assert not create_app().testing
    assert create_app({'TESTING': True}).testing

def test_index(client):
    response = client.get('/')
    assert response.data == b'This is a flask-todo project, not to be used in production.'

def test_status_route(client):
    response = client.get('/status?c=400')
    assert response.status_code == 400

    response = client.get('/status?c=500')
    assert response.status_code == 500

    response = client.get('/status')
    assert response.status_code == 200
