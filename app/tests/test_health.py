import pytest
import json

from app import app
import health

TEST_PROJECT_URL = 'http://example.com/project'
TEST_CONTAINER_URL = 'http://example.com/container'


@pytest.fixture
def client():
    app.config['TESTING'] = True

    app.config['PROJECT_URL'] = TEST_PROJECT_URL
    app.config['CONTAINER_URL'] = TEST_CONTAINER_URL

    with app.app_context():
        yield app.test_client()


def test_health(client):
    """
    Tests `/health` endpoint.
    """
    result = client.get('/health')
    data = json.loads(result.data)

    # test expected data type
    assert isinstance(data, dict)

    # test required fields in response
    assert 'status' in data
    assert 'container' in data
    assert 'project' in data

    # test fields values in response
    assert data['status'] == 'healthy'
    assert data['container'] == TEST_CONTAINER_URL
    assert data['project'] == TEST_PROJECT_URL

    # test data contains only expected fields
    assert len(data.keys()) == 3
