# from __future__ import absolute_import, unicode_literals

import requests
from celery import shared_task
from django.conf import settings

from web.celery import app
from .models import CategoryModel


@shared_task
def start_parsing_shop():
    categories = CategoryModel.objects.all()
    for category in categories:
        requests.post(url=settings.PARSER_URL.format(pk=category.pk, link=category.link))
    print('task 1')


@app.task
def start_handler_product():
    print('task 2')
