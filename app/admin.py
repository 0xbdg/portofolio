from django.contrib import admin
from django.contrib.auth.models import Group
from .models import *

# Register your models here.
admin.site.index_title = "Dashboard"
admin.site.site_header = "Portofolio Dashboard"

class ProjectConf(admin.ModelAdmin):
    list_display = ("image","name","category","description","date")
    list_filter = ["category"]

class ArticleConf(admin.ModelAdmin):
    list_display = ("id","thumbnail","title","description","content","date")

class ContactConf(admin.ModelAdmin):
    list_display = ("username","email","message","date")
    readonly_fields = ("username","email","message","date")

admin.site.unregister(Group)
admin.site.register(tbl_project,ProjectConf)
admin.site.register(tbl_blog,ArticleConf)
admin.site.register(tbl_contact,ContactConf)