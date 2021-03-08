import pytest
import boto3
from moto import mock_dynamodb2

import dynamo_client

TEST_SECRET = 'Lorem ipsum dolor sit amet, consectetur adipiscing elit, ' \
              'sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.'

TEST_CODENAME = 'test-challenge'


@pytest.fixture
def func():
    with mock_dynamodb2():
        # setup aws session
        boto3.setup_default_session(aws_access_key_id='FakeKey',
                                    aws_secret_access_key='FakeSecret',
                                    region_name='us-east-1')
        # Connect to mocked dynamodb, and create table.
        table = boto3.resource('dynamodb', 'us-east-1').create_table(
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

        table.meta.client.get_waiter('table_exists').wait(TableName='devops-challenge')

        # Add expected item
        table.put_item(
            Item={
                'code_name': TEST_CODENAME,
                'secret_code': TEST_SECRET,
            }
        )

        yield dynamo_client.get_dynamo

        # Cleaning up
        table.delete()


def test_dynamo(func):
    """
    Tests get_dynamo endpoint.
    """
    dynamo, table = func('fake_key', 'fake_secret', 'us-east-1')

    # test expected data type
    assert dynamo is not None

    # test required fields in response
    assert table is not None

    response = table.get_item(
        Key={
            'code_name': TEST_CODENAME,
        }
    )

    # testing database data
    assert response['Item']['secret_code'] == TEST_SECRET
