from fastapi.testclient import TestClient

def test_coupons_create(client: TestClient, admin_auth_header):
    response = client.post('/coupons/', headers= admin_auth_header,
                            json = {'code': 'codigo',
                                    'expire_at' : 'datetime',
                                    'limit' : 5,
                                    'type' : 'CouponsType',
                                    'value' : 5.0
                                    })
    
    
    assert response.status_code == 201
    assert response.json()['code'] == 'codigo'
    assert response.json()['expire_at'] == 'datetime'
    assert response.json()['limit'] == 5
    assert response.json()['type'] == 'CouponsType' 
    assert response.json()['value'] == 5.0


def test_coupons_update(client: TestClient, admin_auth_header):
    response = client.post('/coupons/', headers= admin_auth_header,
                            json = {'code': 'codigo',
                                    'expire_at' : 'datetime',
                                    'limit' : 5,
                                    'type' : 'CouponsType',
                                    'value' : 5.0
                                    })
    
    
    assert response.status_code == 201

    response = client.put('/coupons/', headers= admin_auth_header,
                            json = {'code': 'codigo 2',
                                    'expire_at' : 'datetime2',
                                    'limit' : 10,
                                    'type' : 'CouponsType2',
                                    'value' : 6.0
                             })
    assert response.status_code == 200
    assert response.json()['code'] == 'descricao alterada'
    assert response.json()['expire_at'] == 200
    assert response.json()['limit'] == '10'
    assert response.json()['type'] == 'CouponsType2'
    assert response.json()['value'] == 6.0