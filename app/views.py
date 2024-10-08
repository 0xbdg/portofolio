from django.shortcuts import render,redirect
from .forms import *
from .models import *

# Create your views here.
def index(request):
    project = Project.objects.all()
    article = Blog.objects.all()
    return render(request,"pages/home.html", context={'projects':project, 'articles':article})

def article(request):
    return render(request,"pages/article.html",{"items":Blog.objects.all()})

def project(request):
    return render(request,"pages/project.html",{"projects":Project.objects.all()})

def about(request):
    return render(request,"pages/about.html")

def resume(request):
    return render(request, "pages/resume.html")

def success_page(request):
    return render(request, "pages/success_page.html")

def feedback(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("success")
    else:
        form = ContactForm()
    return render(request,"pages/feedback.html",{"forms":form})

def article_detail(request, article_id):
    blog = Blog.objects.get(pk=article_id)
    return render(request,"detail_page/article_detail.html", {"article":blog})