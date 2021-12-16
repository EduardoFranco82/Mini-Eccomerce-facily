from fastapi.testclient import TestClient

def test_customers_create (client: TestClient,   admin_auth_header):
    #user = user_factory()
    response = client.post('/customer/', headers= admin_auth_header,
                             json = {
                                        
                                        'first_name' : 'primeiro nome',
                                        'last_name' : 'segundo nome',
                                        'phone_number' : '33612341',
                                        'genre' : 'm',
                                        'document_id' : '123',
                                        'birth_date' : '1982-06-18',
                                        'user' :  {
                                    "display_name": "jose25",
                                    "email": "jose@",
                                    "password": "123"
                                    
                                    }
                                        
                                    })
    #print(response.json())
    assert response.status_code == 201
    assert response.json()['id'] == 1
    assert response.json()['first_name'] == 'primeiro nome'
    assert response.json()['last_name'] == 'segundo nome'
    assert response.json()['phone_number'] == '33612341'
    assert response.json()['genre'] == 'm'
    assert response.json()['document_id'] == '123'
    assert response.json()['birth_date'] == '1982-06-18'
    #assert response.json()['user_id'] == user.id
    


def test_customers_update (client: TestClient, user_factory, customers_factory , admin_auth_header):
    user = user_factory(role = 'customer')
    customer = customers_factory(user_id = user.id)
    
    

    response = client.put(f'/customer/{customer.id}', headers= admin_auth_header,
                         json= {
                                        'first_name' : 'primeiro nome2',
                                        'last_name' : 'segundo nome2',
                                        'phone_number' : '336123412',
                                        'genre' : 'f',
                                       
                                        'birth_date' : '1982-06-19',
                                        'user' :  {
                                    "display_name": "jose25",
                                    "email": "jose@",
                                    "password": "123",
                                    "id" : user.id
                                    
                                    }
                                })
    
    customer = client.get(f'/customer/{customer.id}', headers= admin_auth_header)
    print(customer.json())

    print(response.json())
    assert response.status_code ==200
    #assert response.json()['id'] == 1
    assert response.json()['first_name'] == 'primeiro nome2'
    assert response.json()['last_name'] == 'segundo nome2'
    assert response.json()['phone_number'] == '336123412'
    assert response.json()['genre'] == 'f'
    assert response.json()['birth_date'] == '1982-06-19'
    