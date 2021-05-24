from django.urls import path, include
from django.conf import settings
from user_profile import views as user_profile_views

app_name = "user_profile"

urlpatterns = [
    
    path('login/', user_profile_views.login_view, name="login"),
    path('registrations/', user_profile_views.user_registrations, name="user_registrations"),
    path('change_password/', user_profile_views.change_password, name="change_password"),
    
]