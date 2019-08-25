FROM python:3.6

COPY ./../../src ./
RUN pip install -r requirements.txt
RUN python manage.py migrate


