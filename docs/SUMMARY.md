# Project summary

### Step by step development log

1. I read INSTRUCTIONS.md from main repo and took time to find out how
to solve task properly.
1. I've never used dynamodb before and now i needed to do some research
about it. I read documentation about dynamo and see how to use this.
I found python libraries for AWS that named `boto3`.
1. I cloned main repo and restructure it as i usually do.
1. Then I prepare development environment - created virtualenv, and
installed necessary dependencies(`pytest`, `flask`, `boto3`, etc).
1. I founded and installed local dynamodb installation for local
testing and experiments during development.
1. After several attempts my code starting worked with the local and
production dynamo. And I got the expected secret code.
1. Then I reformatted the source for testing and wrote tests.
1. Then I wrote `Dockerfile` and `docker-compose.yml` and run it for test
on my own servers.
1. I connected repo to travis-ci and wrote `.travis.yml` to always runs the
automatic tests. I have to solve several problems along the way. And then
this everything turned out okay.
1. I created repo at dockerhub and wrote a script for building and
publishing container from travis.
1. I wrote documentation and this file.
1. At the end I run my code locally for the last time and took the screenshots.

