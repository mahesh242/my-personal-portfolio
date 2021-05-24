from django.urls import path, include
from django.conf import settings
from articles import views as article_view

app_name = "articles"

urlpatterns = [
    path('', article_view.all_articles, name="all_articles"),
    path("<int:blog_id>/", article_view.article_details, name="article_details"),
]