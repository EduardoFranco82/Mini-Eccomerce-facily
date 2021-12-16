from fastapi.testclient import TestClient

def test_address_create (client: TestClient, customers_factory,  admin_auth_header):
    customers = customers_factory()
    response = client.post('/address/', headers= admin_auth_header,
                             json = {
                                        'address': 'endereco',
                                        'city': 'itanhandu',
                                        'state': 'mg',
                                        'number': '5',
                                        'zipcode': '37464000',
                                        'neighbourhood': 'varzea',
                                        'primary': True,
                                        'customer_id': customers.id
                                    })
    print(response.json())
    assert  response.status_code == 201
    assert response.json()['id'] == 1
    assert response.json()['address'] == 'endereco'
    assert response.json()['city'] == 'itanhandu'
    assert response.json()['state'] == 'mg'
    assert response.json()['number'] == '5'
    assert response.json()['zipcode'] == '37464000'
    assert response.json()['neighbourhood'] == 'varzea'
    assert response.json()['primary'] == True
    assert response.json()['customer_id'] == customers.id


def test_address_update (client: TestClient,customers_factory,  admin_auth_header):
    customer = customers_factory()
    response = client.post('/address/', headers= admin_auth_header,
                             json = {
                                        'address': 'endereco',
                                        'city': 'itanhandu',
                                        'state': 'mg',
                                        'number': '5',
                                        'zipcode': '37464000',
                                        'neighbourhood': 'varzea',
                                        'primary': True,
                                        'customer_id': customer.id
                             })
    print(response.json())
    assert  response.status_code == 201

    response = client.put('/address/1', headers= admin_auth_header,
                         json= {
                                        'address': 'outro endereco',
                                        'city': 'passa quatro',
                                        'state': 'mg',
                                        'number': '10',
                                        'zipcode': '37464111',
                                        'neighbourhood': 'copacabana',
                                        'primary': True,
                                        'customer_id': customer.id
                         })
    assert response.status_code ==200
    assert response.json()['id'] == 1
    assert response.json()['address'] == 'outro endereco'
    assert response.json()['city'] == 'passa quatro'
    assert response.json()['state'] == 'mg'
    assert response.json()['number'] == '10'
    assert response.json()['zipcode'] == '37464111'
    assert response.json()['neighbourhood'] == 'copacabana'
    assert response.json()['primary'] == True
    assert response.json()['customer_id'] == customer.id