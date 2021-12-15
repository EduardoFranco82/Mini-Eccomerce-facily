from fastapi.testclient import TestClient


def test_supplier_create(client: TestClient, admin_auth_header):
    response = client.post('/supplier/', headers= admin_auth_header, json={
        'name': 'Supplier 1'
    })

    assert response.status_code == 201
    assert response.json()['id'] == 1


def test_supplier_update(client: TestClient, admin_auth_header):
    response = client.post('/supplier/', headers= admin_auth_header, json={
        'name': 'Supplier 1'
    })
    assert response.status_code == 201

    response = client.put(
        '/supplier/1',headers= admin_auth_header, json={'name': 'Supplier alterado'})

    assert response.status_code == 200
    assert response.json()['name'] == 'Supplier alterado'

    #response = client.get('/categories/1')
    #assert response.json()['name'] == 'Categoria alterada'