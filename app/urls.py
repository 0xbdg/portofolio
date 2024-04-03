from django.urls import path
from .views import *

urlpatterns = [
    path("",index,name="index"),
    path("articles/",article,name="article"),
    path("videos/",video,name="video-player"),
    path("projects/",project,name="project"),
    path("about/",about,name="about"),
    path("feedback/",feedback,name="feedback"),
    path("feedback/success/",success_page,name="success"),
    path("resume/", resume, name="resume"),
    path("articles/<uuid:article_id>",article_detail,name="article-detail")
]
