from django.urls import path, include
from django.conf import settings
from home import views as home_views

app_name = "home"

urlpatterns = [
    path('', home_views.home, name="home"),
#     path('watch_video', home_views.watch_video, name="watch_video"),
    path("<int:video_id>/", home_views.watch_video, name="watch_video"),
]