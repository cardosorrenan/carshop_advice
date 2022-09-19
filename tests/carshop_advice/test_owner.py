import json


def test_list_owner(test_client, headers):
    response = test_client.get('/api/owners/', headers=headers)
    assert response.status_code == 200

def test_get_one_owner(test_client, headers):
    response = test_client.get('/api/owners/1/', headers=headers)
    assert response.status_code == 200

def test_create_owner(test_client, headers):
    data = json.dumps({"firstname": "user2" , 
                       "lastname": "test2",
                       "email": "user2@Tester.com", 
                       "age": 50})
    response = test_client.post('/api/owners/', data=data, headers=headers)
    assert response.status_code == 201
    
def test_update_owner(test_client, headers):
    data = json.dumps({"firstname": "user3" , 
                       "lastname": "test3",
                       "email": "user@test3.com", 
                       "age": 51})
    response = test_client.patch('/api/owners/1/', data=data, headers=headers)
    assert response.status_code == 200

def test_delete_owner(test_client, headers):
    response = test_client.delete('/api/owners/3/', headers=headers)
    assert response.status_code == 204
