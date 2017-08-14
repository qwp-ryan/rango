# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from django.http import HttpResponse

def index(Request):
    return HttpResponse("Rango says hey there partner!")
