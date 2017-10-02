# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from rango.models import UserProfile
# Register your models here.

from .models import *

class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('name',)}
class PageAdmin(admin.ModelAdmin):
    list_display = ('title','category','url',)


admin.site.register(Category, CategoryAdmin)
admin.site.register(Page,PageAdmin)
admin.site.register(UserProfile)
admin.site.register(PassportInformation)
admin.site.register(VisaInformation)