from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"), # Endpoint corresponding to the index view in views.py
]