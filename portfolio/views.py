from django.shortcuts import render
from portfolio.models import Project

def home(request):
    projects = Project.objects.all()
    return render(request, "portfolio/my_portfolio.html", {'projects':projects})