# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from rango.models import Category, Page
from rango.forms import CategoryForm
from .put_log import put_log
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
def show_category(request, category_name_slug):
    context_dict = {}
    try:
        category = Category.objects.get(slug = category_name_slug)
        pages = Page.objects.filter(category = category)
        context_dict['pages'] = pages
        context_dict['category'] = category
    except Category.DoesNotExist:
        context_dict['category'] = None
        context_dict['pages'] = None
    return render(request,'rang/category.html',context_dict)

def add_category(request):
    form=CategoryForm()

    if request.method == 'POST':
        form = CategoryForm(request.POST)

        if form.is_valid():
            cat=form.save(commit=True)
            return index(request)
        else:
            print(form.errors)

    return render(request,'rang/add_category.html',{'form':form})
#def show_detail(request):
#   old_tag = Page.objects.get(page=title)
#    """修改"""
#    if old_tag == new_tag:
#        content = content + msg
#
#    else:
#        content = content + timezone.now + new_tag

def add_Project(request):
    form=CategoryForm()

    if request.method == 'POST':
        form = CategoryForm(request.POST)

        if form.is_valid():
            cat=form.save(commit=True)
            return index(request)
        else:
            print(form.errors)

    return render(request,'rang/add_category.html',{'form':form})
