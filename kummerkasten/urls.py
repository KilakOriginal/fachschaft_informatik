from django.urls import path
from . import views

urlpatterns = [
    path("", views.messageForm, name="kummerkasten-form"),
]
