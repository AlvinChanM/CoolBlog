# -*- coding: utf-8 -*-
from __future__ import unicode_literals


# Register your models here.
from django.contrib import admin
from models import Category, Tag, Article
admin.site.register(Category)
admin.site.register(Tag)


class ArticleAdmin(admin.ModelAdmin):
    list_display = ['title', 'created_time', 'modified_time', 'category', 'author']


admin.site.register(Article)


