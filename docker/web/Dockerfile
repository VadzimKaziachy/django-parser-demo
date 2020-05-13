FROM python:3.7

COPY wait-for-it.sh ./
COPY entrypoint.sh ./
COPY requirements.txt ./

RUN apt-get update && \
    apt-get install -y postgresql-client && \
    pip install --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt
