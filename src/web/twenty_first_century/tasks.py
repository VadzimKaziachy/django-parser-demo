from __future__ import absolute_import, unicode_literals

from celery import shared_task
from web.celery import app


@shared_task
def start_parsing_product():
    print('task 1')


@app.task
def start_handler_product():
    print('task 2')
