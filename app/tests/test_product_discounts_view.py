from fastapi.testclient import TestClient

def test_product_discounts_create (client: TestClient, product_factory, payment_methods_factory, admin_auth_header):
    products = product_factory()
    payment_methods = payment_methods_factory(enabled = True)
    response = client.post('/product_discount/', headers= admin_auth_header,
                             json = {
                                        'mode' : 'value',
                                        'value' : 10.0,
                                        'payment_method_id' : payment_methods.id,
                                        'product_id' : products.id
                             })
    print(response.json())
    assert  response.status_code == 201
    assert response.json()['id'] == 1
    assert response.json()['mode'] == 'value'
    assert response.json()['payment_method_id'] == payment_methods.id
    assert response.json()['product_id'] == products.id
    assert response.json()['value'] == 10.0


def test_product_discounts_update (client: TestClient, product_factory, payment_methods_factory, admin_auth_header):
    products = product_factory()
    payment_methods = payment_methods_factory(enabled = True)
    response = client.post('/product_discount/', headers= admin_auth_header,
                             json = {
                                        'mode' : 'value',
                                        'value' : 10.0,
                                        'payment_method_id' : payment_methods.id ,
                                        'product_id' : products.id
                             })
    assert response.status_code == 201

    response = client.put('/product_discount/1', headers= admin_auth_header,
                         json= {
                                        'mode' : 'percentage',
                                        'value' : 5,
                                        'payment_method_id' : payment_methods.id,
                                        'product_id' : products.id
                         })
    assert response.status_code ==200
    assert response.json()['mode'] == 'percentage'
    assert response.json()['payment_method_id'] == payment_methods.id
    assert response.json()['product_id'] == products.id
    assert response.json()['value'] == 5