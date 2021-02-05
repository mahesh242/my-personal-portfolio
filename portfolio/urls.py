from django.urls import path, include
from django.conf import settings
from . import views

app_name = "portfolio"

urlpatterns = [
    path('', views.home, name="home"),
]