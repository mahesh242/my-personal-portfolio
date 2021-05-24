from django.urls import path, include
from django.conf import settings
from videos import views as videos_views

app_name = "videos"

urlpatterns = [
    path('', videos_views.all_videos, name="all_videos"),
    path("<int:video_id>/", videos_views.watch_video, name="watch_video"),
]