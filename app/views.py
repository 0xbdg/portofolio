from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,"pages/index.html")

def article(request):
    return render(request,"pages/article.html")

def video(request):
    return render(request,"pages/video_player.html")