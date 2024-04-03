from django.urls import path
from .views import *

urlpatterns = [
    path("",index,name="index"),
    path("articles/",article,name="article"),
    path("videos/",video,name="video-player"),
    path("projects/",project,name="project"),
    path("about/",about,name="about"),
    path("contact/",contact,name="contact"),
    path("articles/<uuid:article_id>",article_detail,name="article-detail")
]
