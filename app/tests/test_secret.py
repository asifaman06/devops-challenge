import pytest
import json
import boto3
from moto import mock_dynamodb2

from flask import g

from app import app
import secret

TEST_SECRET = 'Lorem ipsum dolor sit amet, consectetur adipiscing elit, ' \
              'sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.'

TEST_CODENAME = 'test-challenge'


@pytest.fixture
def client():
    app.config['TESTING'] = True
    app.config['CODENAME'] = TEST_CODENAME

    with mock_dynamodb2(), app.app_context():
        # setup aws session
        boto3.setup_default_session(aws_access_key_id='FakeKey',
                                    aws_secret_access_key='FakeSecret',
                                    region_name='us-east-1')
        # Connect to mocked dynamodb
        g.dynamo = boto3.resource('dynamodb', 'us-east-1')

        # Create table.
        g.table = g.dynamo.create_table(
            TableName='devops-challenge',
            KeySchema=[
                {
                    'AttributeName': 'code_name',
                    'KeyType': 'HASH'
                }
            ],
            AttributeDefinitions=[
                {
                    'AttributeName': 'code_name',
                    'AttributeType': 'S'
                },
            ],
            ProvisionedThroughput={
                'ReadCapacityUnits': 5,
                'WriteCapacityUnits': 5
            }
        )

        g.table.meta.client.get_waiter('table_exists').wait(TableName='devops-challenge')

        # Add expected item
        g.table.put_item(
            Item={
                'code_name': TEST_CODENAME,
                'secret_code': TEST_SECRET,
            }
        )

        yield app.test_client()

        # Cleaning up
        g.table.delete()


def test_secret(client):
    """
    Tests `/secret` endpoint.
    """
    result = client.get('/secret')
    data = json.loads(result.data)

    # test expected data type
    assert isinstance(data, dict)

    # test required fields in response
    assert 'secret_code' in data

    # test fields values in response
    assert data['secret_code'] == TEST_SECRET

    # test data contains only expected fields
    assert len(data.keys()) == 1
