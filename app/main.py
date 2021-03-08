from flask import jsonify,abort
from app import app
import os

from botocore.exceptions import ClientError, EndpointConnectionError

import dynamo_client

try:
    # loading configuration environment
    app.config.from_mapping(CODENAME=os.environ['CODENAME'],
                            CONTAINER_URL=os.environ['CONTAINER_URL'],
                            PROJECT_URL=os.environ['PROJECT_URL'])

    dynamo, table = dynamo_client.get_dynamo(os.environ['AWS_KEY'], os.environ['AWS_SECRET'],
                                      os.environ['AWS_REGION'], os.environ.get('DYNAMO_ENDPOINT'))

except KeyError as e:
    # missing configuration environment
    raise RuntimeError('Unable to get configuration env var `%s`' % str(e)) from e

except EndpointConnectionError as e:
    # connection error
    raise RuntimeError('Dynamo is db not available.') from e

except ClientError as e:
    if e.response['Error']['Code'] == 'ResourceNotFoundException':
        # required table not found in dynamodb
        raise RuntimeError('Required table does not exist.') from e
    if e.response['Error']['Code'] in ('UnrecognizedClientException', 'AccessDeniedException'):
        # required table not found in dynamodb
        raise RuntimeError('Dynamo error. Probably your access token is invalid.') from e
    # reraise other exceptions
    raise


@app.route('/health')
def health():
    """\
    This function serves `/health` endpoint.
    Responses service status in json format
    that indicates server working normally.
    """

    response = dict(status='healthy',
                    container=app.config['CONTAINER_URL'],
                    project=app.config['PROJECT_URL'])

    return jsonify(response)

@app.route('/secret')
def secret():
    """\
    This function serves `/secret` endpoint.
    Gets secret code from database then then renders json in response.

    When code not found returns HTTP 500 error.
    """

    try:
        # requesting data from dynamodb
        response = table.get_item(
            Key={
                'code_name': app.config['CODENAME'],
            }
        )

        # extracting secret_code
        secret_code = response['Item']['secret_code']

        # send response
        return jsonify(dict(secret_code=secret_code))
    except KeyError:
        # secret_code was not found, show HTTP 500 error
        abort(500, 'secret_code was not found in database')


if __name__ == '__main__':
    app.run(debug=False)
