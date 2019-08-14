from django.urls import path
from .views import data, datadisplay

urlpatterns = [
    path('', data, name="data"),
    path('datadisplay', datadisplay, name="datadisplay"),
]
