from django.shortcuts import render, get_object_or_404
from master.models import ArticlesMaster
from articles.models import Article


def all_articles(request):
    # articles_master = ArticlesMaster.objects.all()
    articles = Article.objects.order_by('created_date')
    flutter_articles = Article.objects.filter(article_category__category='Flutter').count()
    django_articles = Article.objects.filter(article_category__category='Django').count()
    return render(request,"articles/articles.html",{#'articles_master':articles_master,
                                                    'articles_data':articles,
                                                    'flutter_articles':flutter_articles,
                                                    'django_articles':django_articles,
                                                })

def article_details(request, blog_id):
    blog = get_object_or_404(Article, pk=blog_id)
    return render(request,"articles/articles_details.html",{'blog':blog})