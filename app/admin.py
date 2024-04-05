from django.contrib import admin
from django.contrib.auth.models import Group
from .models import *

# Register your models here.
admin.site.index_title = "Dashboard"
admin.site.site_header = "Portofolio Dashboard"
admin.site.site_title = "Portofolio site admin"

class ProjectConf(admin.ModelAdmin):
    list_display = ("name","image","category","description","date")
    list_filter = ["category"]

class ArticleConf(admin.ModelAdmin):
    list_display = ("title","description","content","thumbnail","date")
    filter_horizontal = ('tags',)

    def tags(self, obj):
        return ", ".join([tag.name for tag in obj.tags.all()])
    tags.short_description = 'Tags'


class ContactConf(admin.ModelAdmin):
    list_display = ("username","email","message","date")
    readonly_fields = ("username","email","message","date")

class VideoConf(admin.ModelAdmin):
    list_display = ("title","video","thumbnail","date")

admin.site.unregister(Group)
admin.site.register(Tag)
admin.site.register(tbl_project,ProjectConf)
admin.site.register(tbl_blog,ArticleConf)
admin.site.register(tbl_feedback,ContactConf)
admin.site.register(tbl_video, VideoConf)