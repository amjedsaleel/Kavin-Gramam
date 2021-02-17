# Django
from django.urls import path

# local Django
from . import views

app_name = 'charity'

urlpatterns = [
    path('', views.index, name='index')
]