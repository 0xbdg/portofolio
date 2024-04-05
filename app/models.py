from django.db import models
from ckeditor.fields import RichTextField
from datetime import datetime
import uuid

PROJECT_TYPE = (
    ("Application","Application"),
    ("Malware","Malware"),
    ("Hardware","Hardware"),
    ("Other","Other")
)

TAGS = (
    ("Tech","Tech"),
    ("Programming","Programming"),
    ('Web Development','Web Development'),
    ('Malware Development', 'Malware Development'),
    ('Malware Analysis','Malware Analysis'),
    ('Reverse Engineering','Reverse Engineering'),
    ('Hardware','Hardware'),
    ('Self Learning', 'Self learning')
)

class Tag(models.Model):
    name = models.CharField(max_length=100,choices=TAGS)

    def __str__(self):
        return self.name

# Create your models here.
class tbl_project(models.Model):
    image = models.ImageField(null=True,blank=True)
    name = models.CharField(max_length=255,null=True)
    category = models.CharField(max_length=50,choices=PROJECT_TYPE,null=True)
    description = models.TextField()
    date = models.DateTimeField(default=datetime.now,editable=False)

class tbl_blog(models.Model):
    id = models.CharField(primary_key=True, default=uuid.uuid4, max_length=36, editable=False)
    thumbnail = models.ImageField(null=True,blank=True)
    title = models.CharField(max_length=255)
    tags = models.ManyToManyField(Tag)
    description = models.CharField(max_length=255)
    content = RichTextField()
    date = models.DateTimeField(default=datetime.now,editable=False)

class tbl_video(models.Model):
    title = models.CharField(max_length=255)
    video = models.FileField(upload_to="videos/", null=True,blank=True)
    thumbnail = models.ImageField(null=True)
    date = models.DateTimeField(default=datetime.now,editable=False)

class tbl_feedback(models.Model):
    username = models.CharField(max_length=50,null=True)
    email = models.EmailField()
    message = models.TextField()
    date = models.DateTimeField(default=datetime.now,editable=False)