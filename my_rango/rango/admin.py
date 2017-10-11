# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from .models import *

# class CategoryAdmin(admin.ModelAdmin):
#     prepopulated_fields = {'slug':('name',)}
# class PageAdmin(admin.ModelAdmin):
#     list_display = ('title','category','url',)


admin.site.register(UserProfile)
admin.site.register(PersonalInformation)
admin.site.register(PassportInformation)
admin.site.register(Plan)
admin.site.register(VisaInformation)
admin.site.register(CountryInformation)
admin.site.register(CityInformation)
admin.site.register(Delegation)
admin.site.register(InvitationInformation)
admin.site.register(Permission)
admin.site.register(BudgetInformation)
admin.site.register(SummaryInformation)
admin.site.register(Reimbursement)
admin.site.register(CardPay)
admin.site.register(TimeTable)
