from django.db import models
from ckeditor.fields import RichTextField
from datetime import datetime

PROJECT_TYPE = (
    ("Application","Application"),
    ("Malware","Malware"),
    ("Hardware","Hardware"),
    ("Other","Other")
)

# Create your models here.
class tbl_project(models.Model):
    image = models.ImageField(null=True,blank=True)
    name = models.CharField(max_length=255,null=True)
    category = models.CharField(max_length=50,choices=PROJECT_TYPE,null=True)
    description = models.TextField()
    date = models.DateTimeField(default=datetime.now,editable=False)

class tbl_blog(models.Model):
    id = models.AutoField(primary_key=True)
    thumbnail = models.ImageField(null=True,blank=True)
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    content = RichTextField()
    date = models.DateTimeField(default=datetime.now,editable=False)

class tbl_video(models.Model):
    title = models.CharField(max_length=255)
    video = models.FileField(upload_to="assets", null=True,blank=True)
    thumbnail = models.ImageField(null=True)
    date = models.DateTimeField(default=datetime.now,editable=False)

class tbl_contact(models.Model):
    username = models.CharField(max_length=50,null=True)
    email = models.EmailField()
    message = models.TextField()
    date = models.DateTimeField(default=datetime.now,editable=False)