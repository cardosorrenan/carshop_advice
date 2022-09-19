import pytest
from flask_jwt_extended import create_access_token

from app import create_app


@pytest.fixture(scope='module')
def test_client():
    app = create_app()
    with app.test_client() as testing_client:
        with app.app_context():
            yield testing_client

@pytest.fixture
def headers():
    authorization = f'Bearer {create_access_token(identity=1)}'
    return {
        'Content-Type': 'application/json',
        'Authorization': authorization,
        'Accept': 'application/json'
    }