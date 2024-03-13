from django.urls import path
from .views import *

urlpatterns = [
    path("",index,name="index"),
    path("articles/",article,name="article"),
    path("videos/",video,name="video-player")
]
