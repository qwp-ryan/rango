# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.template.defaultfilters import slugify
from datetime import timezone
# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=128, unique=True)
    views = models.IntegerField(default=0)
    likes= models.IntegerField(default=0)
    slug = models.SlugField(blank = True, unique = True)

    def save(self, *args, **kwargs):
        self.slug=slugify(self.name)
        super(Category,self).save(*args,**kwargs)

    class Meta:
        verbose_name_plural = 'Categories'
        
    def __str__(self):
        return self.name


class Page(models.Model):
    category = models.ForeignKey(Category)
    title = models.CharField(max_length=128)
    url = models.URLField()
    views = models.IntegerField(default=0)
    likes = models.IntegerField(default=0)

    def __str__(self):
        return self.title


class Process(models.Model):
    states = models.CharField(max_length=128, unique=True)
#    views = models.IntegerField(default=0)
#    likes = models.IntegerField(default=0)
#    class Meta:
#        verbose_name_plural = 'Categories'
    def __str__(self):
        return self.states

class Personal_information(models.Model):
    name=models.CharField(verbose_name = '姓名',max_length=20)
    def __str__(self):
        return self.name

class Project(models.Model):
    Project_id = models.AutoField
    contact_name = models.CharField(max_length=20)
    contact_email = models.EmailField()
    contact_mobil = models.CharField(max_length=13)
    title_zh = models.CharField(max_length=128)
    title_en = models.CharField(verbose_name='英文项目名称', max_length=200)
    research_delegation = models.Choice()
    delegation_tag = choice()
    time_leave = models.DateField(verbose_name='离开中国国境日期', )
    time_back = models.DateField(verbose_name='返回中国国境日期', )
#    Members = models.ManyToManyField(Personal_information, verbose_name='出访人员')
    Task_detail = models.TextField(verbose_name='任务内容以及意义描述', )
    aim = models.CharField(max_length=500)
    task_detail = models.CharField(max_length=500)
    schedule = models.CharField(max_length=500)
    
#    log = models.TextField(verbose_name = '进度记录', blank = True)
#    url = models.URLField()
#    views = models.IntegerField(default=0)
#    likes = models.IntegerField(default = 0)

    def __str__(self):
        return self.title

