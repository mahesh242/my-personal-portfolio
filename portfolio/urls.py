from django.urls import path, include
from django.conf import settings
from portfolio import views as portfolio_views

app_name = "portfolio"

urlpatterns = [
    path('', portfolio_views.home, name="home"),
]