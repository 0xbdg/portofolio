from django.db import models
from ckeditor.fields import RichTextField
from datetime import datetime

PROJECT_TYPE = (
    ("Website","Website"),
    ("Malware","Malware"),
    ("Hardware","Hardware"),
    ("Other","Other")
)

# Create your models here.
class tbl_project(models.Model):
    image = models.ImageField(null=True,blank=True)
    project_name = models.CharField(max_length=255,null=True)
    category = models.CharField(max_length=50,choices=PROJECT_TYPE,null=True)
    description = RichTextField()
    upload_date = models.DateTimeField(default=datetime.now,editable=False)

class tbl_blog(models.Model):
    id = models.AutoField(primary_key=True)
    thumbnail = models.ImageField(null=True,blank=True)
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    content = RichTextField()
    add_date = models.DateTimeField(default=datetime.now,editable=False)

class tbl_video(models.Model):
    pass