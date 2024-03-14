from django.shortcuts import render,redirect
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

def about(request):
    return render(request,"pages/about.html")

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success_page')  # Redirect to a success page
    else:
        form = ContactForm()
    return render(request,"pages/contact.html",{"forms":form})