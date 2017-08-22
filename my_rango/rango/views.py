# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from django.http import HttpResponse

def index(Request):
    context_dict={'boldmessage':"Crunch, creamy, cookie, candy, cupcake!"}
    return render(Request, 'rang/index.html', context = context_dict)
#    return HttpResponse("Rango says hey there partner! <br/> <a href='/rango/about/'> About </a>")

def about(Request):
    context_dict={'newmessage': "about page of Django!"}
    return render(Request, 'rang/about.html', context = context_dict)
    #return HttpResponse("Rango says here is the about page <br/> <a href='/rango/'> Index </a>")