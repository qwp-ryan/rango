# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from .choices import *
from django.db import models
from django.template.defaultfilters import slugify
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
    user = models.OneToOneField(User)
    website = models.URLField(blank=True)
    picture = models.ImageField(upload_to='profile_images', blank=True)

    def __str__(self):
        return self.user.username


class PersonalInformation(models.Model):
    name = models.CharField(verbose_name='姓名', max_length=10)
    tel = models.CharField(verbose_name='电话', max_length=12)
    email = models.EmailField()
    gender = models.CharField(verbose_name='性别', max_length=1, choices=GENDER_CHOICES)
    department = models.CharField(verbose_name='所在部门', max_length=30)
    ID_num = models.CharField(verbose_name='18位身份证号', max_length=18)
    Place_of_Birth = models.CharField(verbose_name='出生地（省）', max_length=2, choices=PLACE_CHOICES)
    Date_of_Birth = models.DateField(verbose_name='出生日期', null=True, blank=True)
    duty = models.CharField(verbose_name='职务', max_length=1, choices=duty_choices)
    identity = models.CharField(verbose_name='对外身份', max_length=1, choices=identity_choices)
    race = models.CharField(verbose_name='民族', max_length=2, choices=race_choices)
    political_identity = models.CharField(verbose_name='政治面貌', max_length=2, choices=political_choices)
    securety = models.CharField(verbose_name='涉密等级', max_length=1, choices=securety_choices)
    status_health = models.CharField(verbose_name='健康状况', max_length=1, choices=health_choices)
    emergency_contact_name = models.CharField(verbose_name='紧急联系人姓名', max_length=10)
    emergency_contact_tel = models.CharField(max_length=11)

    def __str__(self):
        return self.name


class PassportInformation(models.Model):
    person = models.ForeignKey(PersonalInformation, on_delete=models.CASCADE)
    passport_number = models.CharField(verbose_name='护照号码', max_length=15)
    date_issue = models.DateField(verbose_name='颁发日期', null=True, blank=True)
    date_expire = models.DateField(verbose_name='过期日期', null=True, blank=True)
    issue_office = models.CharField(verbose_name='发证机关', max_length=15)
    issue_place = models.CharField(verbose_name='发证地点', max_length=15)
    date_out = models.DateField(verbose_name='借出日期', null=True, blank=True)
    date_back = models.DateField(verbose_name='归还日期', null=True, blank=True)

    def __str__(self):
        return self.passport_number


class VisaInformation(models.Model):
    Passport = models.ForeignKey(PassportInformation)
    country = models.CharField(verbose_name='国家', max_length=20)
    issue_date = models.DateField(verbose_name='颁发日期', null=True, blank=True)
    expire_date = models.DateField(verbose_name='过期日期', null=True, blank=True)
    visa_class = models.CharField(verbose_name='签证类型', choices=visa_choices, max_length=1)
    visa_file = models.FileField(verbose_name='签证扫描件', upload_to='upload/%Y/%M/')

    def __str__(self):
        return self.country


class CountryInformation(models.Model):
    name = models.CharField(verbose_name='国家简称', max_length=20)
    cash = models.CharField(verbose_name='外汇种类', max_length=1, choices=cash_choices)
    visa_requirement = models.TextField(verbose_name='办理签证所需材料')

    def __str__(self):
        return self.name


class CityInformation(models.Model):
    country = models.ForeignKey(CountryInformation)
    city = models.CharField(verbose_name='', max_length=50)
    short_meal = models.IntegerField(verbose_name='伙食费标准', null=True, blank=True)
    short_accom = models.IntegerField(verbose_name='住宿费标准', null=True, blank=True)
    short_work = models.IntegerField(verbose_name='公杂费标准', null=True, blank=True)
    study_high = models.IntegerField(verbose_name='高级访问标准', null=True, blank=True)
    study_middle = models.IntegerField(verbose_name='中级访问标准', null=True, blank=True)
    study_student = models.IntegerField(verbose_name='研究学生标准', null=True, blank=True)

    def __str__(self):
        if self.city == '所有城市':
            return self.country.name
        else:
            return self.country.name+' - '+self.city


class Delegation(models.Model):
    contact_name = models.ManyToManyField(User)
    contact_mobile = models.CharField(max_length=11)
    title = models.CharField(max_length=128)
    title_en = models.CharField(verbose_name='英文项目名称', max_length=200)
    country = models.ManyToManyField(CountryInformation, verbose_name='出访国家')
    destination = models.ManyToManyField(CityInformation, verbose_name='出访目的地')
    time_leave = models.DateField(verbose_name='离开中国国境日期', )
    time_back = models.DateField(verbose_name='返回中国国境日期', )
    Members = models.ManyToManyField(PersonalInformation, verbose_name='出访人员')
    Task = models.CharField(verbose_name='出访目的250字', max_length=500)
    mission = models.CharField(verbose_name='出访任务500字', max_length=1000)
    research_delegation = models.CharField(
        max_length=1,
        verbose_name='是否为教学科研团组',
        choices=delegation_choices,
        default='A',
    )
    delegation_tag = models.CharField(
        max_length=2,
        verbose_name='团组类型',
        choices=delegation_tag_choices,
    )
    time_arrangement = models.CharField(verbose_name='详细日程安排', max_length=1000)
    finacial = models.CharField(verbose_name='课题卡号, 多个课题卡以分号隔开', max_length=100)
    budget_abroad = models.IntegerField(verbose_name='境外预算')
    budget_internal = models.IntegerField(verbose_name='国内预算')
    process = models.CharField(verbose_name='团组进程', choices=process_tag, max_length=2, default='01')
    unexpected = models.CharField(verbose_name='团组特殊情况', max_length=1, choices=unexpected_tag, default='1')
    log = models.TextField(verbose_name='进度记录', blank=True)

    def save(self, *args, **kwargs):
        self.slug=slugify(self.country.all()[0].name+''+self.time_leave.strftime('%Y-%m-%d')+''+self.Members.all()[0].name)
        #[0]+self.Members[0]+self.time_leave  将date格式转换成了string格式，以便成为slug
        #引用方法请注意，self.country.all()[0].name
        super(Delegation,self).save(*args,**kwargs)

    def __str__(self):
        return self.country.all()[0].name+''+self.time_leave.strftime('%Y-%m-%d')+''+self.Members.all()[0].name  #self.country[0]+self.Members[0]+
        #return self.slug  错误的，另一个函数中定义的，这个不能用。


class InvitationInformation(models.Model):
    delegation = models.ForeignKey(Delegation)
    time_start = models.DateField(verbose_name='邀请信上开始时间')
    time_end = models.DateField(verbose_name='邀请信上结束时间')
    member = models.ManyToManyField(PersonalInformation, verbose_name='被邀请人')
    invitor = models.CharField(verbose_name='邀请人', max_length=100)
    tel = models.CharField(verbose_name='邀请方电话', max_length=30)
    address = models.CharField(verbose_name='邀请方英文地址', max_length=400)
    Institue_CH = models.CharField(verbose_name='邀请单位中文名称', max_length=200)
    Insitute_EN = models.CharField(verbose_name='邀请单位英文名称', max_length=200)
    invitation_letter = models.FileField(verbose_name='', upload_to='upload/%Y/%m/')


class Permission(models.Model):
    delegation = models.ForeignKey(Delegation)
    inner_permit = models.FileField(verbose_name='所内审批表扫描件', upload_to='upload/%Y/%m/')
    cas_permit = models.FileField(verbose_name='院批件', upload_to='upload/%Y/%m/')
    cas_permit_number = models.CharField(verbose_name='院批件文号', max_length=20, null=True, blank=True)

    def __str__(self):
        return self.cas_permit_number


class BudgetInformation(models.Model):
    Delegation = models.ForeignKey(Delegation)
    Budget_meal = models.IntegerField(verbose_name='伙食费（外币）')
    Budget_accom = models.IntegerField(verbose_name='住宿费（外币）')
    Budget_work = models.IntegerField(verbose_name='公杂费（外币）')
    Budget_transition = models.IntegerField(verbose_name='城际间交通费（外币）', null=True, blank=True)
    Budget_conference = models.IntegerField(verbose_name='会议注册费（外币）', null=True, blank=True)


class SummaryInformation(models.Model):
    Delegation = models.ForeignKey(Delegation)
    date_leave = models.DateField(verbose_name='实际离境日期')
    date_back = models.DateField(verbose_name='实际抵境日期')
    cities = models.ManyToManyField(CityInformation, verbose_name='实际访问城市')
    summary = models.TextField(verbose_name='出访总结')
    passport = models.FileField(verbose_name='护照、出入境章扫描件', upload_to='upload/%Y/%m/')
    receipt = models.FileField(verbose_name='发票扫描件', upload_to='upload/%Y/%m/')
    picture = models.FileField(verbose_name='工作照片', upload_to='upload/%Y/%m/')
    fee_meal = models.IntegerField(verbose_name='实际伙食费（外币）')
    fee_accom = models.FloatField(verbose_name='实际住宿费（外币）')
    fee_work = models.IntegerField(verbose_name='实际工杂费（外币）')
    fee_transition = models.FloatField(verbose_name='实际城际间交通费（外币）')
    fee_conference = models.FloatField(verbose_name='实际会议注册费（外币）')


class Reimbursement(models.Model):
    fee_meal_yan = models.FloatField(verbose_name='伙食费(人民币)')
    fee_accom_uam = models.FloatField(verbose_name='住宿费(人民币)')
    fee_work_yan = models.FloatField(verbose_name='工杂费(人民币)')
    fee_transition_yan = models.FloatField(verbose_name='城际间交通费(人民币)')
    fee_conference_yan = models.FloatField(verbose_name='会议注册费(人民币)')
    cash_check = models.FileField(verbose_name='外汇核销表', upload_to='upload/%Y/%m/')
    fee_international = models.FloatField(verbose_name='国际旅费')
    fee_insurance = models.FloatField(verbose_name='保险费')
    fee_visa = models.FloatField(verbose_name='签证费')
    fee_transition = models.FloatField(verbose_name='市内交通费')
    total = models.FloatField(verbose_name='合计')
    def __str__(self):
        return self.total


class CardPay(models.Model):
    Reim = models.ForeignKey(Reimbursement)
    Card_num = models.CharField(verbose_name='课题卡号', max_length=20)
    total = models.FloatField(verbose_name='国际交流费总金额')
    current = models.FloatField(verbose_name='剩余国际交流费金额')
    amount = models.FloatField(verbose_name='报销金额')

    def __str__(self):
        return self.Card_num + ' : ' + self.amount

class Plan(models.Model):
    person = models.ForeignKey(PersonalInformation)
    country = models.ManyToManyField(CountryInformation)
    elegation_tag = models.CharField(
        max_length=2,
        verbose_name='团组类型',
        choices=delegation_tag_choices,
    )
    date_out = models.DateField(verbose_name='拟出访日期')
    days_out = models.IntegerField(verbose_name='拟出访天数')
    finacial = models.IntegerField(verbose_name='所需经费额')


class TimeTable(models.Model):
    delegation = models.ForeignKey(Delegation)
    submit_time = models.DateField(verbose_name='提交申请时间')
    public_time = models.DateField(verbose_name='公示时间')
    arp_input = models.DateField(verbose_name='arp填写时间')
    inner_permit = models.DateField(verbose_name='所内审批时间')
    arp_to_cas = models.DateField(verbose_name='arp上报时间')
    cas_permit = models.DateField(verbose_name='批件下达时间')
    finger_print_date = models.DateField(verbose_name='外办留指纹时间')
    new_passport_date = models.DateField(verbose_name='办理新护照时间')
    visa_infee_date = models.DateField(verbose_name='交签证费时间')
    visa_in_date = models.DateField(verbose_name='送办签证时间')
    visa_finger_date = models.DateField(verbose_name='领馆留指纹时间')
    visa_out_date = models.DateField(verbose_name='获得批件时间')
    visa_fee_date = models.DateField(verbose_name='退还签证费时间')
    cash_date = models.DateField(verbose_name='申请外事借款时间')
    summary_date = models.DateField(verbose_name='提交总结时间')
    summary_pub_date = models.DateField(verbose_name='事后公示时间')
    passport_back_date = models.DateField(verbose_name='归还护照时间')
    cash_check_date = models.DateField(verbose_name='外汇核销时间')
    rmb_reimburse_date = models.DateField(verbose_name='完成报销时间')
