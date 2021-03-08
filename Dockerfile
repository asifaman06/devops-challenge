FROM python:3.9.2-alpine



RUN apk update && \
    apk add --no-cache ca-certificates alpine-sdk yaml-dev linux-headers libffi-dev openssl-dev curl && \
    pip install --upgrade pip 
    
COPY app/requirements.txt /opt/app/requirements.txt
RUN pip install -r /opt/app/requirements.txt

COPY app/ /opt/app/

WORKDIR /opt/app

RUN adduser -D -H -s sbin/nologin thedoctor

EXPOSE 5000

CMD uwsgi --uid thedoctor --gid thedoctor --master --need-app --chdir /opt/app/ --wsgi-file main.py --callable app --http 0.0.0.0:5000 --processes 5 --threads 2