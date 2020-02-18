FROM python:3.7

COPY wait-for-it.sh ./
COPY entrypoint.sh ./

RUN apt-get update && apt-get install -y postgresql-client

RUN pip install --upgrade pip
