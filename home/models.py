# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Category(models.Model):
    # 分类名称
    name = models.CharField(max_length=50, verbose_name="分类名称")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '分类'
        verbose_name_plural = '分类列表'  # verbose_name


class Tag(models.Model):
    # 名称
    name = models.CharField(max_length=50, verbose_name='标签名称')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '标签'
        verbose_name_plural = '标签列表'


class Article(models.Model):
    # 文章标题
    title = models.CharField(max_length=70, verbose_name=u"文章标题")
    # 文章内容
    body = models.TextField(verbose_name='文章内容', default='')
    # 创建时间
    created_time = models.DateTimeField(verbose_name='创建时间', default='')
    # 修改数据
    modified_time = models.DateTimeField(verbose_name='修改时间', default='')
    # 摘要 blank=True 此字段值可以为空
    excerpt = models.CharField(max_length=200, blank=True, verbose_name='摘要')
    # 分类 传入Category类实例化ForeignKey，来描述一对多关系
    category = models.ForeignKey(Category, verbose_name='分类')
    # 标签
    tags = models.ManyToManyField(Tag, blank=True, verbose_name='标签')
    # 作者 ,从django.contrib.auth.models 中导入User作为外键
    author = models.ForeignKey(User, verbose_name='作者')
    # 浏览量 PositiveIntegerField正整数
    views = models.PositiveIntegerField(default=0, verbose_name='浏览量')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = '文章'
        verbose_name_plural = '文章列表'