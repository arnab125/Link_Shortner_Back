from .models import url
from rest_framework import serializers
from .serializers import urlSerializer

from .views import *
from django.urls import path

urlpatterns = [
    path('create/', url_list, name='url_list'),
    path('<str:short_url>/', get, name='get')
]