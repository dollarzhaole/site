__author__ = 'dollar'
#!/usr/bin/python
from tinymce.widgets import TinyMCE
from django.contrib import admin
from sblog.models import Author, Blog, Tag
from django.db import models


class AuthorAdmin(admin.ModelAdmin):
    """docstring for AuthorAdmin"""
    list_display = ('name', 'email', 'website')
    search_fields = ('name',)


class BlogAdmin(admin.ModelAdmin):
    """docstring for BlogAdmin"""
    list_display = ('caption', 'id', 'author', 'publish_time')
    list_filter = ('publish_time',)
    date_hierarchy = 'publish_time'
    ordering = ('-publish_time',)
    filter_horizontal = ('tags',)
    raw_id_fields = ('author',)
    # formfield_overrides = {
    #     models.TextField: {"widget" : TinyMCE},
    #     }
    class Media:
        js = [
            '/static/js/tiny_mce/tiny_mce_src.js',
            '/static/js/tiny_mce/tiny_mce_config.js',
            ]


admin.site.register(Author, AuthorAdmin)
admin.site.register(Blog, BlogAdmin)
admin.site.register(Tag)
