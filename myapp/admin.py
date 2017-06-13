# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from  models import UserInfo,UserType,News,NewsType,Chat,Reply

admin.site.register(UserInfo)
admin.site.register(UserType)
admin.site.register(NewsType)
admin.site.register(News)
admin.site.register(Chat)
admin.site.register(Reply)

# Register your models here.
