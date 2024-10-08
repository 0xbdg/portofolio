from django.contrib import admin
from django.contrib.auth.models import Group
from .models import *

class ProjectConf(admin.ModelAdmin):
    list_display = ("name","image","category","description","date")
    list_filter = ["category"]

class ArticleConf(admin.ModelAdmin):
    list_display = ("title",'author',"date")
    filter_horizontal = ('tags',)

    def tags(self, obj):
        return ", ".join([tag.name for tag in obj.tags.all()])
    tags.short_description = 'Tags'


class ContactConf(admin.ModelAdmin):
    list_display = ("username","email","message","date")
    readonly_fields = ("username","email","message","date")

admin.site.unregister(Group)
admin.site.register(Tag)
admin.site.register(Project,ProjectConf)
admin.site.register(Blog,ArticleConf)
admin.site.register(Feedback,ContactConf)