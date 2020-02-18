from django.urls import path

from . import views

app_name = 'vek'
urlpatterns = [
    path('', views.ScrapyView.as_view(), name='vek'),
]
