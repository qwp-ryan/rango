# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, reverse
from .models import Category, Page
from .forms import CategoryForm, PageForm
from .forms import UserForm, UserProfileForm
from .put_log import put_log
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth import authenticate, login
from django.core.urlresolvers import reverse

def index(Request):
    category_list = Category.objects.order_by('-likes')[:5]
    context_dict={'categories':category_list}
    return render(Request, 'rang/index_1.html', context = context_dict)
#    return HttpResponse("Rango says hey there partner! <br/> <a href='/rango/about/'> About </a>")

def about(Request):
    print(Request.method)
    print(Request.user)
    context_dict={'newmessage': "about page of Django!"}
    #return render(Request, 'rang/about.html', context = context_dict)
    return render(Request, 'rang/about_1.html', context=context_dict)

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
    return render(request,'rang/category_1.html',context_dict)

def add_category(request):
    form=CategoryForm()

    if request.method == 'POST':
        form = CategoryForm(request.POST)

        if form.is_valid():
            cat=form.save(commit=True)
            return index(request)
        else:
            print(form.errors)

    return render(request,'rang/add_category_1.html',{'form':form})

def add_page(request, category_name_slug):
    try:
        category=Category.objects.get(slug=category_name_slug)
    except Category.DoesNotExist:
        category = None


    form=PageForm()

    if request.method == 'POST':
        form = PageForm(request.POST)
        if form.is_valid():
            if category:
                page=form.save(commit=False)
                page.category=category
                page.views=0
                page.save()
                return show_category(request, category_name_slug)
        else:
            print(form.errors)
    context_dict={'form': form, 'category':category}
    return render(request,'rang/add_page_1.html',context_dict)


def add_Project(request):
    form=CategoryForm()

    if request.method == 'POST':
        form = CategoryForm(request.POST)

        if form.is_valid():
            cat=form.save(commit=True)
            return index(request)
        else:
            print(form.errors)

    return render(request,'rang/add_category_1.html',{'form':form})

def register(request):
    registered=False
    if request.method=='POST':
        user_form=UserForm(data=request.POST)
        profile_form=UserProfileForm(data=request.POST)
        if user_form.is_valid() and profile_form.is_valid():
            user= user_form.save()
            user.set_password(user.password)
            user.save()
            profile=profile_form.save(commit=False)
            profile.user=user
            if 'picture' in request.FILES:
                profile.picture=request.FILES['picture']
            profile.save()
            registered=True
        else:
            print(user_form.errors, profile_form.errors)
    else:
        user_form=UserForm()
        profile_form=UserProfileForm()
    return render(request,
                  'rang/register.html',
                  {'user_form':user_form,
                   'profile_form':profile_form,
                   'registered':registered})


def user_login(request):
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        user=authenticate(username=username, password=password)
        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect(reverse('index'))
            else:
                return HttpResponse("Your Rango account is disabled")
        else:
            print("Invalid login details:{0},{1}".format(username, password))
            return HttpResponse("Invalid login details supplied")
    else:
        return render(request, 'rang/login.html',{})
