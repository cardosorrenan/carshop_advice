import json


def test_user_login(test_client, headers):
    data = json.dumps({"email": "user@test.com" , "password": "1234"})
    response = test_client.post('/api/auth/login/', 
                                data=data, 
                                headers=headers)
    assert response.status_code == 200