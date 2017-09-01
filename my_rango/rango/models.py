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
    likes = models.IntegerField(default = 0)

    def __str__(self):
        return self.title


class Process(models.Model):
    name = models.CharField(max_length=128, unique=True)
#    views = models.IntegerField(default=0)
#    likes = models.IntegerField(default=0)

    slug = models.SlugField(blank=True, unique=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Process, self).save(*args, **kwargs)

#    class Meta:
#        verbose_name_plural = 'Categories'
    def __str__(self):
        return self.name

class Project(models.Model):
    category = models.ForeignKey(Category)
    title = models.CharField(max_length=128)
    title_en = models.CharField(verbose_name='英文项目名称', max_length=200)
    time_leave = models.DateField(verbose_name='离开中国国境日期', )
    time_back = models.DateField(verbose_name='返回中国国境日期', )
    Members = models.ManyToManyField(Personal_information, verbose_name='出访人员')
    Task_detail = models.TextField(verbose_name='任务内容以及意义描述', )
    log = models.TextField(verbose_name = '进度记录', blank = True)
#    url = models.URLField()
#    views = models.IntegerField(default=0)
#    likes = models.IntegerField(default = 0)


    def __str__(self):
        return self.title