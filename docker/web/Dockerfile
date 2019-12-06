FROM python:3.7

COPY requirements.txt ./
COPY wait-for-it.sh ./

RUN apt-get update
RUN apt-get install -y postgresql-client

RUN pip install --upgrade pip
RUN pip install -r requirements.txt
