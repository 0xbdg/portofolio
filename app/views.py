from django.shortcuts import render
from .forms import *

# Create your views here.
def index(request):
    return render(request,"pages/home.html")

def article(request):
    return render(request,"pages/article.html")

def video(request):
    return render(request,"pages/video_player.html")

def project(request):
    return render(request,"pages/project.html")