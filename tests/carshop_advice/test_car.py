import json


def test_list_car(test_client, headers):
    response = test_client.get('/api/cars/', headers=headers)
    assert response.status_code == 200

def test_get_one_car(test_client, headers):
    response = test_client.get('/api/cars/1/', headers=headers)
    assert response.status_code == 200

def test_create_car(test_client, headers):
    data = json.dumps({"model": "Sedan" , 
                       "color": "Blue",
                       "owner_id": 2, 
                       "available": 1})
    response = test_client.post('/api/cars/', data=data, headers=headers)
    assert response.status_code == 201
    
def test_update_car(test_client, headers):
    data = json.dumps({"model": "Convertible" , 
                       "color": "Gray",
                       "owner_id": 1, 
                       "available": 0})
    response = test_client.patch('/api/cars/1/', data=data, headers=headers)
    assert response.status_code == 200

def test_delete_car(test_client, headers):
    response = test_client.delete('/api/cars/1/', headers=headers)
    assert response.status_code == 204