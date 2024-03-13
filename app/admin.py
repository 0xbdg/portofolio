from django.contrib import admin
from django.contrib.auth.models import Group
from .models import *

# Register your models here.
admin.site.index_title = "Dashboard"
admin.site.site_header = "Portofolio Dashboard"

class ProjectConf(admin.ModelAdmin):
    list_display = ("image","project_name","category","description","upload_date")

class ArticleConf(admin.ModelAdmin):
    list_display = ("id","thumbnail","title","description","content","add_date")

admin.site.unregister(Group)
admin.site.register(tbl_project,ProjectConf)
admin.site.register(tbl_blog,ArticleConf)