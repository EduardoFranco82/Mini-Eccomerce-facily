from fastapi.testclient import TestClient

def test_payment_methods_create (client: TestClient, admin_auth_header):
    response = client.post('/payment_methods/', headers= admin_auth_header,
                             json = {
                                 'name': 'Cartao',
                                 'enabled': True
                             })
    assert response.status_code == 201
    assert response.json()['id'] == 1
    assert response.json()['name'] == 'Cartao'
    assert response.json()['enabled'] == True


def test_payment_methods_update (client: TestClient, admin_auth_header):
    response = client.post('/payment_methods/', headers= admin_auth_header,
                             json = {
                                 'name': 'Cartao',
                                 'enabled': True
                             })
    assert response.status_code == 201

    response = client.put('/payment_methods/1', headers= admin_auth_header,
                         json= {
                             'name': 'Cheque',
                             'enabled': False
                         })
    assert response.status_code ==200
    assert response.json()['name'] == 'Cheque'
    assert response.json()['enabled'] == False