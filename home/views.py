# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse
from django.shortcuts import render
from home.models import Article
# Create your views here.


def index(request):
    # 在settings中配置了templates的路径，此时需要传入index.html的相对路径
    # 获取Artilce表中所有的数据，并按created_time倒序排序,'-'代表倒序
    articles = Article.objects.all().order_by('-created_time')
    return render(request, 'home/index.html', context={'article': articles})

