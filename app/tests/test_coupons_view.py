from fastapi.testclient import TestClient

def test_coupons_create(client: TestClient, admin_auth_header):
    response = client.post('/coupons/', headers= admin_auth_header,
                            json = {'code': 'codigo',
                                    'expire_at' : '1982-06-18 12:00:00',
                                    'limit' : 5,
                                    'type' : 'value',
                                    'value' : 5.0
                                    })
    
    
    assert response.status_code == 201
    assert response.json()['code'] == 'codigo'
    assert response.json()['expire_at'] == '1982-06-18T12:00:00'
    assert response.json()['limit'] == 5
    assert response.json()['type'] == 'value' 
    assert response.json()['value'] == 5.0


def test_coupons_update(client: TestClient, admin_auth_header):
    response = client.post('/coupons/', headers= admin_auth_header,
                            json = {'code': 'codigo',
                                    'expire_at' : '1982-06-18 12:00:00',
                                    'limit' : 5,
                                    'type' : 'value',
                                    'value' : 5.0
                                    })
    
    
    assert response.status_code == 201

    response = client.put('/coupons/1', headers= admin_auth_header,
                            json = {
                                    'expire_at' : '2000-06-18 12:00:00',
                                    'limit' : 10,
                                    
                             })
    assert response.status_code == 200
    
    assert response.json()['expire_at'] == '2000-06-18T12:00:00'
    assert response.json()['limit'] == 10
    