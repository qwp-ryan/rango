# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.

from rango.models import Category, Page

class PageAdmin(admin.ModelAdmin):
    list_display = ('title','category','url',)
admin.site.register(Category)
admin.site.register(Page,PageAdmin)