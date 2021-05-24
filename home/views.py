from django.shortcuts import render
from portfolio.models import Project
from articles.models import Article
from videos.models import Videos

def home(request):
    projects = Project.objects.all()
    
    flutter_articles = Article.objects.filter(article_category__category='Flutter').order_by('created_date')[:2]
    django_articles = Article.objects.filter(article_category__category='Django').order_by('created_date')[:2]
    linux_articles = Article.objects.filter(article_category__category='Linux').order_by('created_date')[:2]

    all_videos = Videos.objects.order_by('created_date')[:2]
    return render(request,"home/home.html",{'projects':projects,
                                            'flutter_articles':flutter_articles,
                                            'django_articles':django_articles,
                                            'linux_articles':linux_articles,
                                            'all_videos':all_videos,
                                        })
                

def watch_video(request, video_id=None):
    video = Videos.objects.filter(id=video_id)
    return render(request,"videos/video_details.html",{'video':video})
