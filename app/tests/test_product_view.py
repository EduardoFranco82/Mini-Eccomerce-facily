from fastapi.testclient import TestClient
from .conftest import category_factory, supplier_factory


def test_product_create(client: TestClient, category_factory, supplier_factory, admin_auth_header):
    category = category_factory()
    supplier = supplier_factory()

    response = client.post('/product/', headers=admin_auth_header,
                           json={
                               'description': 'descricao',
                               'price': 100,
                               'image': 'image.dev',
                               'technical_details': 'bla bla',
                               'visible': True,
                               'categorie_id': category.id,
                               'supplier_id': supplier.id
                           })

    assert response.status_code == 201
    assert response.json()['description'] == 'descricao'
    assert response.json()['price'] == 100
    assert response.json()['categorie_id'] == category.id
    assert response.json()['supplier_id'] == supplier.id

def test_product_update(client: TestClient, category_factor: category_factory, supplier_factory: supplier_factory, admin_auth_header):
    category = category_factor()
    supplier = supplier_factory()
    
    response = client.post('/product/', headers=admin_auth_header,
                           json={
                               'description': 'descricao',
                               'price': 100,
                               'image': 'image.dev',
                               'technical_details': 'bla bla',
                               'visible': True,
                               'categorie_id': category.id,
                               'supplier_id': supplier.id
                           })

    assert response.status_code == 201

    response = client.put('/product/1', headers=admin_auth_header,
                           json={
                               'description': 'descricao alterada',
                               'price': 200,
                               'image': 'image.dev2',
                               'technical_details': 'bla bla bla',
                               'visible': True,
                               'categorie_id': category.id,
                               'supplier_id': supplier.id
                           })
   
   
    assert response.status_code == 200
    assert response.json()['description'] == 'descricao alterada'
    assert response.json()['price'] == 200
    assert response.json()['image'] == 'image.dev2'
    assert response.json()['technical_details'] == 'bla bla bla'
    assert response.json()['visible'] == True
    assert response.json()['categorie_id'] == category.id
    assert response.json()['supplier_id'] == supplier.id


