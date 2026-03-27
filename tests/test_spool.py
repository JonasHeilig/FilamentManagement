import pytest
from app import create_app
from models import db


@pytest.fixture
def client():
    app = create_app({'TESTING': True, 'SQLALCHEMY_DATABASE_URI': 'sqlite:///:memory:'})
    with app.app_context():
        db.create_all()
        yield app.test_client()


def test_create_spool(client):
    resp = client.post('/api/spools', json={
        'name': 'TestSpool',
        'material': 'PLA',
        'color': 'Red',
        'total_weight_grams': 500
    })
    assert resp.status_code == 201
    data = resp.get_json()
    assert data['name'] == 'TestSpool'
    assert data['remaining_weight_grams'] == 500


def test_consume_spool(client):
    # create
    resp = client.post('/api/spools', json={
        'name': 'Consumable',
        'material': 'PETG',
        'color': 'Blue',
        'total_weight_grams': 300
    })
    assert resp.status_code == 201
    spool = resp.get_json()
    sid = spool['id']

    # consume 100
    resp2 = client.post(f'/api/spools/{sid}/consume', json={'grams': 100})
    assert resp2.status_code == 200
    data2 = resp2.get_json()
    assert data2['actual_consumed'] == 100
    assert data2['remaining'] == 200

    # consume more than remaining
    resp3 = client.post(f'/api/spools/{sid}/consume', json={'grams': 500})
    assert resp3.status_code == 200
    data3 = resp3.get_json()
    assert data3['actual_consumed'] == 200
    assert data3['remaining'] == 0
