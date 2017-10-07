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


class PersonalInformation(models.Model):
    name=models.CharField(verbose_name='姓名', max_length=10)
    tel = models.CharField(verbose_name='电话', max_length=12)
    email = models.EmailField()
    gender = models.CharField(verbose_name='性别', max_length=1, choices=GENDER_CHOICES)
    department = models.CharField(verbose_name='所在部门', max_length=30)
    ID_num = models.CharField(verbose_name='18位身份证号', max_length=18)
    Place_of_Birth = models.CharField(verbose_name='出生地（省）', max_length=2, choices=PLACE_CHOICES)
    Date_of_Birth = models.DateField(verbose_name='出生日期', null=True, blank=True)
    duty = models.CharField(verbose_name='职务', max_length=1, choices=duty_choices)
    identity = models.CharField(verbose_name='对外身份', max_length=1, choices=identity_choices)
    race = models.CharField(verbose_name='民族', max_length =2, choices=race_choices)
    political_identity = models.CharField(verbose_name='政治面貌', max_length=2, choices=political_choices)
    securety = models.CharField(verbose_name='涉密等级', max_length=1, choices=securety_choices)
    status_health = models.CharField(verbose_name='健康状况', max_length=1, choices=health_choices)
    emergency_contact_name = models.CharField(verbose_name='紧急联系人姓名', max_length=10)
    emergency_contact_tel = models.CharField(max_length=11)
    def __str__(self):
        return self.name


class PassportInformation(models.Model):
    person = models.ForeignKey(PersonalInformation)
    passport_number = models.CharField(verbose_name='护照号码', max_length=15, unique=True)
    date_issue = models.DateField(verbose_name='颁发日期')
    date_expire = models.DateField(verbose_name='过期日期')
    issue_office = models.CharField(verbose_name='发证机关', max_length=15)
    issue_place = models.CharField(verbose_name='发证地点', max_length=15)
    date_out = models.DateField(verbose_name='借出日期', null=True, blank=True)
    date_back = models.DateField(verbose_name='归还日期', null=True, blank=True)

    def __str__(self):
        return self.passport_number


class VisaInformation(models.Model):
    Passport = models.ForeignKey(PassportInformation)
    country = models.CharField(verbose_name='国家', max_length=20)
    issue_date = models.DateField(verbose_name='颁发日期')
    expire_date = models.DateField(verbose_name='过期日期')
    visa_class = models.CharField(verbose_name='签证类型', choices=visa_choices, max_length=1)
    visa_file = models.FileField(verbose_name='签证扫描件', upload_to='upload/%Y/%m/')

    def __str__(self):
        return self.country
