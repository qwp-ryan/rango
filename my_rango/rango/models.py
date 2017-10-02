# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from .choices import *
from django.db import models
from django.template.defaultfilters import slugify
from datetime import timezone
from django.contrib.auth.models import User

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


class UserProfile(models.Model):
    user=models.OneToOneField(User)
    website=models.URLField(blank=True)
    picture=models.ImageField(upload_to='profile_images',blank=True)

    def __str__(self):
        return self.user.username


class PassportInformation(models.Model):
    name = models.CharField(verbose_name='姓名', max_length=10)
    birth_date = models.DateField(verbose_name='出生日期')
    birth_place = models.CharField(verbose_name='出生地', max_length=2, choices=PLACE_CHOICES)
    gender = models.CharField(verbose_name='性别', max_length=1, choices=GENDER_CHOICES)
    passport_number = models.CharField(verbose_name='护照号码', max_length=15, unique=True)
    date_issue = models.DateField(verbose_name='颁发日期')
    date_expire = models.DateField(verbose_name='过期日期')
    issue_office = models.CharField(verbose_name='发证机关', max_length=15)
    issue_place = models.CharField(verbose_name='发证地点', max_length=15)
    date_out = models.DateField(verbose_name='借出日期', null=True, blank=True)
    date_back = models.DateField(verbose_name='归还日期', null=True, blank=True)

    # def save(self, *args, **kwargs):
    #     self.slug = slugify(self.Passport_number)
    #     super(PassportInformation, self).save(*args, **kwargs)

    def __str__(self):
        return self.name


class VisaInformation(models.Model):
    Passport = models.ForeignKey(PassportInformation)
    country = models.CharField(verbose_name='国家', max_length=20)
    issue_date = models.DateField(verbose_name='颁发日期')
    expire_date = models.DateField(verbose_name='过期日期')
    visa_class = models.CharField(verbose_name='签证类型', choices=visa_choices, max_length=1)
    visa_file = models.FileField(verbose_name='签证扫描件', upload_to='upload/%Y/%m/')

    def __str__(self):
        return self.country
