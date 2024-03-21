from django.shortcuts import render,redirect
from .forms import *
from .models import *

# Create your views here.
def index(request):
    return render(request,"pages/home.html")

def article(request):
    return render(request,"pages/article.html",{"items":tbl_blog.objects.all()})

def video(request):
    return render(request,"pages/video_player.html")

def project(request):
    return render(request,"pages/project.html",{"projects":tbl_project.objects.all()})

def about(request):
    return render(request,"pages/about.html")

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("success_page")
    else:
        form = ContactForm()
    return render(request,"pages/contact.html",{"forms":form})

def article_detail(request):
    return render(request,"detil_page/article_detail.html")