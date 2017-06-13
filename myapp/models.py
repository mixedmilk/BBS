# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
class UserType(models.Model):
    role=models.CharField(max_length=50)
    def __str__(self):
        return self.role

class UserInfo(models.Model):
    username=models.CharField(max_length=50)
    password=models.CharField(max_length=50)
    email=models.CharField(max_length=50)
    user_type=models.ForeignKey(UserType)
    def __str__(self):
        return self.username

class NewsType(models.Model):
    newstype=models.CharField(max_length=50)
    def __str__(self):
        return self.newstype
class News(models.Model):
    title=models.CharField(max_length=500)
    url=models.CharField(max_length=500)
    category=models.ForeignKey(NewsType)
    overview=models.TextField()
    createtime=models.DateTimeField()
    favor_count=models.IntegerField(default=0)
    comment_count=models.IntegerField(default=0)
    def __str__(self):
        return self.title
class Chat(models.Model):
    user=models.ForeignKey(UserInfo)
    sendtime=models.DateTimeField()
    content=models.CharField(max_length=100)
    def __str__(self):
        return self.user
class Reply(models.Model):
    user = models.ForeignKey(UserInfo)
    comment_time=models.DateTimeField()
    tonews=models.ForeignKey(News)
    comment=models.TextField()
    def __str__(self):
        return self.user





# Create your models here.
