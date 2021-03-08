# How to run

Before you run the application you must provide proper credentials in `application.env`.
See `application.env.template` for an example.

### application.env

`application.env` must contains following values:

* CODENAME - codename of project, for example `thedoctor`.
* AWS_KEY - AWS access key.
* AWS_SECRET - AWS access secret.
* AWS_REGION - Using AWS region, usually `us-east-1`.
* CONTAINER_URL - Url of project's github, for example `https://github.com/asifaman06/devops-challenge`.
* PROJECT_URL - Url of project's dockerhub, for example `https://hub.docker.com/r/asifaman06/devops-challenge`

### Application port

Make sure you don't use port 5000 on host machine for other purpose. If you need to 
use another port, edit `docker-compose.yml`.

### Run from prebuilt container

You may use provided `docker-compose.yml` to run prebuilt container from dockerhub.
Following commands will start everything you needed:

```bash
wget https://raw.githubusercontent.com/asifaman06/devops-challenge/master/application.env.tamplate
wget https://raw.githubusercontent.com/asifaman06/devops-challenge/master/docker-compose.yml
mv application.env.tamplate application.env
vim application.env
docker-compose -d up
```

### Build and run manually

In an alternative way you may build and run container manually using following commands:

```bash
docker build -t application ./
docker run -p 127.0.0.1:5000:5000 -d --restart on-failure --env-file application.env --name application application
```

### Troubleshooting

For information about troubleshooting see **[Trouble](TROUBLE.md)**.
