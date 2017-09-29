# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.template.defaultfilters import slugify
from datetime import timezone
from django.contrib.auth.models import User
# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=128, unique=True)
    views = models.IntegerField(default=0)
    likes = models.IntegerField(default=0)
    slug = models.SlugField(blank=True, unique=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Category, self).save(*args, **kwargs)

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


class Delegation(models.Model):
    research_delegation_choices = (
        ('A', '教学科研类团组'),
        ('B', '非教学科研类团组'),
    )
    delegation_tag_choices = (
        ('01', '合作研究'),
        ('02', '学术访问'),
        ('03', '出席国际会议'),
        ('04', '教学活动'),
        ('05', '科学观测'),
        ('06', '科学考察'),
        ('07', '科研仪器调试'),
        ('08', '科技展览'),
        ('09', '出席国际组织活动'),
        ('10', '人才招聘'),
        ('11', '其他'),
    )
    contact_name = models.OneToOneField(User)
    contact_mobile = models.CharField(max_length=11)
    title = models.CharField(max_length=128)
    title_en = models.CharField(verbose_name='英文项目名称', max_length=200)
    destination = models.ManyToManyField(DestinationInformation, verbose_name='出访目的地')
    time_leave = models.DateField(verbose_name='离开中国国境日期', )
    time_back = models.DateField(verbose_name='返回中国国境日期', )
    Members = models.ManyToManyField(PersonalInformation, verbose_name='出访人员')
    Task = models.CharField(verbose_name='出访目的', max_length=500)
    mission = models.CharField(verbose_name='出访任务', max_length=1000)
    research_delegation = models.CharField(
        max_length=1,
        verbose_name='是否为教学科研团组',
        choices=research_delegation_choices,
        default='A',
    )
    delegation_tag = models.CharField(
        max_length=2,
        verbose_name='团组类型',
        choices=delegation_tag_choices,
    )

    time_arrangement = models.CharField(verbose_name='详细日程安排', max_length=1000)
    finace_support = models.CharField(verbose_name='课题卡号, 多个课题卡以分号隔开', max_length=100)
    budget_abroad = models.IntegerField(verbose_name='境外预算')
    budget_internal = models.IntegerField(verbose_name='国内预算')
    log = models.TextField(verbose_name='进度记录', blank=True)

    def __str__(self):
        return self.title


class DestinationInformation(models.Model):
    destination_choices = (
        (1, '蒙古'),
        (2, '朝鲜'),
        (3, (
            (1, '韩国-首尔、釜山、济州'),
            (2, '韩国-光州，西归浦'),
            (3, '韩国-其他城市'),
           )),
        (4, (
             (1, '美国-华盛顿'),
             (2, '美国-旧金山'),
             (3, '美国-休斯顿'),
             (4, '美国-波士顿'),
             (5, '美国-纽约'),
             (6, '美国-芝加哥'),
             (7, '美国-洛杉矶'),
             (8, '美国-夏威夷'),
             (9, '美国-其他城市'),
            )),
    )
    name_intitute = models.CharField(verbose_name='邀请机构中文名称', max_length=100)
    name_en_institute = models.CharField(verbose_name='邀请机构英文名称', max_length=100)
    introduction = models.CharField(verbose_name='邀请机构简介', max_length=1000)
    date_start = models.DateField(verbose_name='访问开始时间')
    date_end = models.DateField(verbose_name='访问结束时间')
    destination = models.IntegerField(verbose_name='请选择出访目的地', choices=destination_choices)
    invitor = models.CharField(verbose_name='邀请人', max_length=50)
    address_en = models.CharField(verbose_name='邀请单位地址', max_length=200)
    tel = models.CharField(verbose_name='邀请人电话', max_length=12)
    invitation_letter = models.FileField(verbose_name='邀请信', upload_to='upload/%Y/%m/')


class PersonalInformation(models.Model):
    gender_choices = (
        ('M', 'Male'),
        ('F', 'Female'),
    )
    place_choices = (
        ('SH', '上海市'),
        ('BJ', '北京市'),
        ('SD', '山东省'),
        ('HL', '黑龙江省'),
        ('JL', '吉林省'),
        ('LN', '辽宁省'),
        ('HB', '河北省'),
        ('NM', '内蒙古自治区'),
        ('TJ', '天津市'),
        ('SX', '山西省'),
        ('SH', '陕西省'),
        ('GS', '甘肃省'),
        ('XJ', '新疆维吾尔自治区'),
        ('QH', '青海省'),
        ('HE', '河南省'),
        ('NX', '宁夏回族自治区'),
        ('XZ', '西藏自治区'),
        ('SC', '四川省'),
        ('BH', '湖北省'),
        ('HU', '湖南省'),
        ('JS', '江苏省'),
        ('ZJ', '浙江省'),
        ('AH', '安徽省'),
        ('FJ', '福建省'),
        ('YN', '云南省'),
        ('GZ', '贵州省'),
        ('GD', '广东省'),
        ('GX', '广西壮族自治区'),
        ('CQ', '重庆市'),
        ('HA', '海南省'),
        ('JX', '江西省'),
        ('JW', '境外')
    )
    duty_choices = (
        ('A', '所长'),
        ('B', '副所长'),
        ('C', '书记'),
        ('D', '无'),
    )
    identity_choices = (
        ('A', '研究员'),
        ('B', '副研究员'),
        ('C', '助理研究员'),
        ('D', '工程师'),
        ('E', '高级工程师'),
        ('F', '正高级工程师'),
        ('G', '博士后、在读学生'),
    )
    race_choices = (
        ('01', '汉族'),
        ('02', '满族'),
        ('03', '回族'),
        ('04', '藏族'),
        ('05', '壮族'),
        ('06', '其他'),
    )
    political_choices = (
        ('01', '中共党员'),
        ('02', '中共预备党员'),
        ('03', '共青团员'),
        ('04', '民革党员'),
        ('05', '民盟盟员'),
        ('06', '民建会员'),
        ('07', '民进会员'),
        ('08', '农工党党员'),
        ('09', '致公党党员'),
        ('10', '九三学社社员'),
        ('11', '台盟盟员'),
        ('12', '无党派人士'),
        ('13', '群众'),
    )
    securety_choices = (
        ('A', '绝密'),
        ('B', '机密'),
        ('C', '秘密'),
        ('D', '不涉密'),
    )
    health_choices = (
        ('A', '健康'),
        ('B', '一般'),
        ('C', '较差'),
    )
    name = models.CharField(verbose_name='姓名', max_length=20)
    tel = models.CharField(verbose_name='电话', max_length=12)
    email = models.EmailField()
    gender = models.CharField(verbose_name='性别', choices=gender_choices, max_length=1)
    department = models.CharField(verbose_name='所在部门', max_length=30)
    ID_num = models.CharField(verbose_name='18位身份证号', max_length=18)
    Place_of_Birth = models.CharField(verbose_name='出生地（省）', max_length=2, choices=place_choices)
    Date_of_Birth = models.DateField(verbose_name='出生日期')
    duty = models.CharField(verbose_name='职务', max_length=1, choices=duty_choices)
    identity = models.CharField(verbose_name='对外身份', max_length=1, choices=identity_choices)
    race = models.CharField(verbose_name='民族', max_length=2, choices=race_choices)
    political_identity = models.CharField(verbose_name='政治面貌', max_length=2, choices=political_choices)
    securety = models.CharField(verbose_name='涉密等级', max_length=1, choices=securety_choices)
    status_health = models.CharField(verbose_name='健康状况', max_length=1, choices=health_choices)
    emergency_contact_name = models.CharField(verbose_name='紧急联系人姓名', max_length=10)
    emergency_contact_tel = models.CharField(max_length=11)
    family_member = models.TextField()
#    father=
#    mother=
#    wife=
#    son=
#    daughter=
#    age=
#    political_identity_2=
#    institute=

    def __str__(self):
        return self.name


class PassportInformation(models.Model):
    Passport_number = models.CharField(verbose_name='护照号码', max_length=15)
    date_issue = models.DateField(verbose_name='颁发日期')
    date_expire = models.DateField(verbose_name='过期日期')
    issue_office = models.CharField(verbose_name='发证机关', max_length=15)
    issue_place = models.CharField(verbose_name='发证地点', max_length=15)
    date_out = models.DateField(verbose_name='借出日期')
    date_back = models.DateField(verbose_name='归还日期')


class VisaInformation(models.Model):
    visa_choices = (
        ('A', '一次入境签证'),
        ('B', '多次入境签证'),
    )
    Passport_number = models.ForeignKey(PassportInformation)
    coutry = models.CharField(verbose_name='国家', max_length=2)
    issue_date = models.DateField(verbose_name='颁发日期')
    expire_date = models.DateField(verbose_name='过期日期')
    visa_class = models.CharField(verbose_name='签证类型', choices=visa_choices, max_length=1)
    visa_file = models.FileField(verbose_name='签证扫描件', upload_to='upload/%Y/%m/')


class InforVisa(models.Model):
    coutry = models.CharField(verbose_name='国家', max_length=2)
    requirement = models.TextField(verbose_name='签证材料列表')


class PermitInformation(models.Model):
    inner_permit = models.FileField(verbose_name='所内审批表扫描件', upload_to='upload/%Y/%m/')
    cas_permit = models.FileField(verbose_name='院批件', upload_to='upload/%Y/%m/')
    cas_permit_number = models.CharField(verbose_name='院批件文号', max_length=20)


class SupportStandard(models.Model):
    coutry = models.CharField(verbose_name='国家', max_length=2)
    city = models.CharField(verbose_name='城市', max_length=2)
    cash_category = models.CharField(verbose_name='外汇种类', max_length=2)
    eating = models.FloatField(verbose_name='伙食标准每人每天')
    accomodation = models.FloatField(verbose_name='住宿标准每人每天')
    others = models.FloatField(verbose_name='公杂标准每人每天')
    high_standard = models.FloatField(verbose_name='留学高级访问学者每人每月')
    standard = models.FloatField(verbose_name='留学访问学者每人每月')
    student_standard = models.FloatField(verbose_name='留学研究生每人每月')


class CashBudget(models.Model):
    transition = models.IntegerField(verbose_name='城市间')
    conference_fee = models.IntegerField(verbose_name='会议注册费')


class Summary(models.Model):
    leave_date = models.DateField(verbose_name='实际离境日期')
    arrive_date = models.DateField(verbose_name='实际入境日期')
    cities = models.CharField(verbose_name='实际访问城市路线', max_length=300)
    passport = models.FileField(verbose_name='护照信息扫描件', upload_to='upload/%Y/%m/')
    visa = models.FileField(verbose_name='签证+出入境章扫描件', upload_to='upload/%Y/%m/')
    summary = models.TextField(verbose_name='归后总结',)
    picture = models.FileField(verbose_name='工作照片', upload_to='upload/%Y/%m/')
    cash_category = models.CharField(verbose_name='外汇种类', max_length=1)
    eating = models.FloatField(verbose_name='伙食费')
    accomadation = models.FloatField(verbose_name='住宿费')
    other = models.FloatField(verbose_name='公杂费')
    transition = models.FloatField(verbose_name='城市间交通费')
    meeting_registraion = models.FloatField(verbose_name='会议注册费')
    exchange_rate = models.FloatField(verbose_name='兑换汇率费')


class Reimburse(models.Model):
    eating = models.FloatField(verbose_name='伙食费')
    accomodation = models.FloatField(verbose_name='住宿费')
    other = models.FloatField(verbose_name='公杂费')
    transition = models.FloatField(verbose_name='城市间交通费')
    meeting_registration = models.FloatField(verbose_name='会议注册费')
    check_sheet = models.FileField(verbose_name='外汇兑换表扫描件', upload_to='upload/%Y/%m/')
    air_ticket = models.FloatField(verbose_name='国际旅费')
    insurance = models.FloatField(verbose_name='保险费')
    visa_fee = models.FloatField(verbose_name='签证费')
    transition_inner = models.FloatField(verbose_name='国内旅费')
    summary = models.FloatField(verbose_name='总计')
    support_card = models.CharField(verbose_name='课题卡：报销金额；')


class TimeTable(models.Model):
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


class NewPlan(models.Model):
    name = models.OneToOneField(User)
    contry = models.CharField(verbose_name='国家', max_length=2)
    category = models.CharField(verbose_name='分类', max_length=2)
    time = models.DateField(verbose_name='出访时间',)
    period = models.IntegerField(verbose_name='出访时长', default=0)
    budget = models.IntegerField(verbose_name='预算')
    finacial_support = models.CharField(verbose_name='课题卡号,多个课题卡以分号隔开', max_length=100)