# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from rango.models import Category

from django.http import HttpResponse

def index(Request):
    category_list = Category.objects.order_by('-likes')[:5]
    context_dict={'categories':category_list}
    return render(Request, 'rang/index.html', context = context_dict)
#    return HttpResponse("Rango says hey there partner! <br/> <a href='/rango/about/'> About </a>")

def about(Request):
    context_dict={'newmessage': "about page of Django!"}
    return render(Request, 'rang/about.html', context = context_dict)
    #return HttpResponse("Rango says here is the about page <br/> <a href='/rango/'> Index </a>")