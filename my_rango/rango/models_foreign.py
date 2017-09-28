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
    research_delegation_choices=(
        ('A','教学科研类团组'),
        ('B','非教学科研类团组'),
    )
    delegation_tag_choices=(
        ('01','合作研究'),
        ('02','学术访问'),
        ('03','出席国际会议'),
        ('04','教学活动'),
        ('05','科学观测'),
        ('06','科学考察'),
        ('07','科研仪器调试'),
        ('08','科技展览'),
        ('09','出席国际组织活动'),
        ('10','人才招聘'),
        ('11','其他'),
    )
    Project_id = models.AutoField
    contact_name = models.CharField(max_length=20)
    contact_email = models.EmailField()
    contact_mobil = models.CharField(max_length=13)
    title_zh = models.CharField(max_length=128)
    title_en = models.CharField(verbose_name='英文项目名称', max_length=200)
    research_delegation =models.CharField(
        max_length=1,
        verbose_name='是否为教学科研团组',
        choices=research_delegation_choices,
        default=A,
    )
    delegation_tag = models.CharField(
        max_length=2,
        verbose_name='团组类型',
        choices=delegation_tag_choices,
    )
    time_leave = models.DateField(verbose_name='离开中国国境日期',)
    time_back = models.DateField(verbose_name='返回中国国境日期',)
#    Members = models.ManyToManyField(Personal_information, verbose_name='出访人员')
#    Task_detail = models.TextField(verbose_name='任务内容以及意义描述',)
    aim = models.CharField(verbose_name='出访目的',max_length=500)
    task_detail = models.CharField(verbose_name='出访任务',max_length=500)
    schedule = models.CharField(verbose_name='出访行程安排',max_length=500)

#    log = models.TextField(verbose_name = '进度记录', blank = True)
#    url = models.URLField()
#    views = models.IntegerField(default=0)
#    likes = models.IntegerField(default = 0)

    def __str__(self):
        return self.title

class Personal_information(models.Model):
    name=models.CharField(verbose_name = '姓名',max_length=20)
    tel=models.CharField(verbose_name='电话', max_length=12)
    email=models.EmailField()
    gender=
    department=
    ID_num=
    Place_of_Birth=
    Date_of_Birth=
    duty=
    identity=
    race=
    political_identity=
    maintain_secrey=ChoiceField
    status_health=
    emergency_contact_name=
    emergency_contact_tel=
    father=
    mother=
    wife=
    son=
    daughter=
    age=
    political_identity_2=
    institute=
    def __str__(self):
        return self.name

class Passport_information(models.Model):
    Passport_number=
    date_issue=
    date_expire=
    issue_office=
    issue_place=
    date_out=
    date_back=

class visa_information(models.Model):
    Passport_number=models.ForeignKey(Passport_information)
    coutry=
    issue_date=
    expire_date=
    visa_class=
    visa_file=


class Destination_information(models.Model):
    name_intitute=
    name_en_institute=
    introduction=
    date_start=
    date_end=
    country=
    city=
    invitor=
    address_en=
    tel=
    invitation_letter=file=


class Delegation(models.Model):
    contact_name=models.OneToOneField(User)
    contact_mobile=models.CharFiled(max_length=11)
    title = models.CharField(max_length=128)
    title_en = models.CharField(verbose_name='英文项目名称', max_length=200)
    destination=models.ManyToManyField(Destination_information,verbose_name='出访目的地')
    time_leave = models.DateField(verbose_name='离开中国国境日期', )
    time_back = models.DateField(verbose_name='返回中国国境日期', )
    Members = models.ManyToManyField(Personal_information, verbose_name='出访人员')
    Task = models.TextField(verbose_name='出访目的 ', )
    mission=models.TextField(verbose_naem='出访任务',)
    time_arrangement=
    finace_support=
    budget_abroad=
    budget_internal=
    log = models.TextField(verbose_name = '进度记录', blank = True)
#    url = models.URLField()
#    views = models.IntegerField(default=0)
#    likes = models.IntegerField(default = 0)
    def __str__(self):
        return self.title


class Permit_information():
    inner_permit=file
    cas_permit=file
    cas_permit_number=

class information_for_visa():
    coutry=
    requirement=models.TextField()

class support_standard():
    coutry=models.ForeignKey(Contry)
    city=
    cash_category=
    eating=
    accomodation=
    others=
    high_standard=
    standard=
    student_standard=

class Cash_budget():
    transition=
    conference_fee=

class Summary():
    leave_date=
    arrive_date=
    cities=
    passport=file
    visa=file
    summary=text
    picture=
    cash_category=
    eating=
    accomadation=
    other=
    transition=
    meeting_registraion=

class reimburse():
    eating=
    accomodation=
    other=
    transition=
    meeting_registration=
    check_sheet=file
    air_ticket=
    insurance=
    visa_fee=
    transition_inner=
    summary=
    support_card=
    support_amount=

class time_table():
    submit_time=
    public_time=
    arp_input=
    inner_permit=
    arp_to_cas=
    cas_permit=
    finger_print_date=
    new_passport_date=
    visa_in_date=
    visa_finger_date=
    visa_out_date=
    visa_fee_date=
    cash_date=
    summary_date=
    passport_back_date=
    cash_check_date=
    rmb_reimburse_date=

class aborad_plane():
    name=
    gender=
    duty=
    department=
    contry=
    category=
    time=
    period=
    finacial_support=