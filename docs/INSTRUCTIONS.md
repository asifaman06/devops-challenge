# Instructions of development

Fell free to clone and play with this project.

### Project structure

* `/app` contains application code.
* `/app/tests` contains unittests.
* `/docs` contains documentation.
* `/screenshot` contains example screenshots.

### Requirements

Application code is written in Python 3.7.
You should create `virtualenv` and install python requirements from
`/app/requirements.txt` with following command:

```bash
python -m pip install app/requirements.txt
``` 

### Run code

To run code go to application folder and run:

```bash
python -m main.py
```

### Run tests

Use `pytest` for unittesting. To run tests you should go
to application folder and run following command:

```bash
python -m pytest
```

All tests mocked and no additional dependencies required.

### Using local dynamodb installation

You can test code in pre-production environment by using local version 
of dynamodb. For instructions how to install local dynamodb see documentation
from amazon: [Setting Up DynamoDB Local](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/DynamoDBLocal.html).

To run application with local dynamodb you must provide environment variables like this:

```
# Project codename
CODENAME=thedoctor

# AWS access credentials
AWS_KEY=FakeKey
AWS_SECRET=FakeSecret
AWS_REGION=us-east-1

# Project urls
CONTAINER_URL=https://hub.docker.com/r/asifaman06/devops-challenge
PROJECT_URL=https://github.com/asifaman06/devops-challenge

#Dynamo endpoint
DYNAMO_ENDPOINT=http://localhost:8000
```

Notice the `DYNAMO_ENDPOINT`. This override dynamodb
endpoint to local installation.

Fill database with expected values and run code.
