from django.db import models
from ckeditor.fields import RichTextField
from datetime import datetime
from django.contrib.auth.models import User
from django.utils.safestring import mark_safe

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
class Project(models.Model):
    image = models.ImageField(null=True,blank=True)
    name = models.CharField(max_length=255,null=True)
    category = models.CharField(max_length=50,choices=PROJECT_TYPE,null=True)
    description = models.TextField()
    date = models.DateTimeField(default=datetime.now,editable=False)

class Blog(models.Model):
    id = models.CharField(primary_key=True, default=uuid.uuid4, max_length=36, editable=False)
    thumbnail = models.ImageField(null=True,blank=True)
    title = models.CharField(max_length=255)
    tags = models.ManyToManyField(Tag)
    description = models.CharField(max_length=255)
    author = models.ForeignKey(User,on_delete=models.CASCADE,max_length=255)
    content = RichTextField()
    date = models.DateTimeField(default=datetime.now,editable=False)

    def thumbnail(self):
        return mark_safe("<img src='{}' width='100px' height='100px'>".format(self.thumbnail.url))

class Feedback(models.Model):
    username = models.CharField(max_length=50,null=True)
    email = models.EmailField()
    message = models.TextField()
    date = models.DateTimeField(default=datetime.now,editable=False)