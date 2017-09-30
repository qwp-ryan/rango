from __future__ import unicode_literals
from django.db import models
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User


# class PersonalInformation(models.Model):
#     gender_choices = (
#         ('M', 'Male'),
#         ('F', 'Female'),
#     )
#     place_choices = (
#         ('SH', '上海市'),
#         ('BJ', '北京市'),
#         ('SD', '山东省'),
#         ('HL', '黑龙江省'),
#         ('JL', '吉林省'),
#         ('LN', '辽宁省'),
#         ('HB', '河北省'),
#         ('NM', '内蒙古自治区'),
#         ('TJ', '天津市'),
#         ('SX', '山西省'),
#         ('SH', '陕西省'),
#         ('GS', '甘肃省'),
#         ('XJ', '新疆维吾尔自治区'),
#         ('QH', '青海省'),
#         ('HE', '河南省'),
#         ('NX', '宁夏回族自治区'),
#         ('XZ', '西藏自治区'),
#         ('SC', '四川省'),
#         ('BH', '湖北省'),
#         ('HU', '湖南省'),
#         ('JS', '江苏省'),
#         ('ZJ', '浙江省'),
#         ('AH', '安徽省'),
#         ('FJ', '福建省'),
#         ('YN', '云南省'),
#         ('GZ', '贵州省'),
#         ('GD', '广东省'),
#         ('GX', '广西壮族自治区'),
#         ('CQ', '重庆市'),
#         ('HA', '海南省'),
#         ('JX', '江西省'),
#         ('JW', '境外')
#     )
#     duty_choices = (
#         ('A', '所长'),
#         ('B', '副所长'),
#         ('C', '书记'),
#         ('D', '无'),
#     )
#     identity_choices = (
#         ('A', '研究员'),
#         ('B', '副研究员'),
#         ('C', '助理研究员'),
#         ('D', '工程师'),
#         ('E', '高级工程师'),
#         ('F', '正高级工程师'),
#         ('G', '博士后、在读学生'),
#     )
#     race_choices = (
#         ('01', '汉族'),
#         ('02', '满族'),
#         ('03', '回族'),
#         ('04', '藏族'),
#         ('05', '壮族'),
#         ('06', '其他'),
#     )
#     political_choices = (
#         ('01', '中共党员'),
#         ('02', '中共预备党员'),
#         ('03', '共青团员'),
#         ('04', '民革党员'),
#         ('05', '民盟盟员'),
#         ('06', '民建会员'),
#         ('07', '民进会员'),
#         ('08', '农工党党员'),
#         ('09', '致公党党员'),
#         ('10', '九三学社社员'),
#         ('11', '台盟盟员'),
#         ('12', '无党派人士'),
#         ('13', '群众'),
#     )
#     securety_choices = (
#         ('A', '绝密'),
#         ('B', '机密'),
#         ('C', '秘密'),
#         ('D', '不涉密'),
#     )
#     health_choices = (
#         ('A', '健康'),
#         ('B', '一般'),
#         ('C', '较差'),
#     )
#     name = models.CharField(verbose_name='姓名', max_length=20)
#     tel = models.CharField(verbose_name='电话', max_length=12)
#     email = models.EmailField()
#     gender = models.CharField(verbose_name='性别', choices=gender_choices, max_length=1)
#     department = models.CharField(verbose_name='所在部门', max_length=30)
#     ID_num = models.CharField(verbose_name='18位身份证号', max_length=18)
#     Place_of_Birth = models.CharField(verbose_name='出生地（省）', max_length=2, choices=place_choices)
#     Date_of_Birth = models.DateField(verbose_name='出生日期')
#     duty = models.CharField(verbose_name='职务', max_length=1, choices=duty_choices)
#     identity = models.CharField(verbose_name='对外身份', max_length=1, choices=identity_choices)
#     race = models.CharField(verbose_name='民族', max_length=2, choices=race_choices)
#     political_identity = models.CharField(verbose_name='政治面貌', max_length=2, choices=political_choices)
#     securety = models.CharField(verbose_name='涉密等级', max_length=1, choices=securety_choices)
#     status_health = models.CharField(verbose_name='健康状况', max_length=1, choices=health_choices)
#     emergency_contact_name = models.CharField(verbose_name='紧急联系人姓名', max_length=10)
#     emergency_contact_tel = models.CharField(max_length=11)
#     family_member = models.TextField()
# #    father=
# #    mother=
# #    wife=
# #    son=
# #    daughter=
# #    age=
# #    political_identity_2=
# #    institute=
#
#     def __str__(self):
#         return self.name


class PassportInformation(models.Model):
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
    )
    PLACE_CHOICES = (
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
    name = models.CharField(verbose_name='姓名', max_length=10)
    birth_date = models.DateField(verbose_name='出生日期')
    birth_place = models.CharField(verbose_name='出生地', max_length=2, choices=PLACE_CHOICES)
    gender = models.CharField(verbose_name='性别', max_length=1, choices=GENDER_CHOICES)
    passport_number = models.CharField(verbose_name='护照号码', max_length=15, unique=True)
    date_issue = models.DateField(verbose_name='颁发日期')
    date_expire = models.DateField(verbose_name='过期日期')
    issue_office = models.CharField(verbose_name='发证机关', max_length=15)
    issue_place = models.CharField(verbose_name='发证地点', max_length=15)
    date_out = models.DateField(verbose_name='借出日期')
    date_back = models.DateField(verbose_name='归还日期')

    # def save(self, *args, **kwargs):
    #     self.slug = slugify(self.Passport_number)
    #     super(PassportInformation, self).save(*args, **kwargs)

    def __str__(self):
        return self.name


class VisaInformation(models.Model):
    visa_choices = (
        ('A', '一次入境签证'),
        ('B', '多次入境签证'),
    )
    Passport = models.ForeignKey(PassportInformation)
    country = models.CharField(verbose_name='国家', max_length=20)
    issue_date = models.DateField(verbose_name='颁发日期')
    expire_date = models.DateField(verbose_name='过期日期')
    visa_class = models.CharField(verbose_name='签证类型', choices=visa_choices, max_length=1)
    visa_file = models.FileField(verbose_name='签证扫描件', upload_to='upload/%Y/%m/')

    def __str__(self):
        return self.country

# class InforVisa(models.Model):
#     coutry = models.CharField(verbose_name='国家', max_length=2)
#     requirement = models.TextField(verbose_name='签证材料列表')
#
#
# class DestinationInformation(models.Model):
#     destination_choices = (
#         (1, '蒙古'),
#         (2, '朝鲜'),
#         (3, (
#             (1, '韩国-首尔、釜山、济州'),
#             (2, '韩国-光州，西归浦'),
#             (3, '韩国-其他城市'),
#            )),
#         (4, (
#              (1, '美国-华盛顿'),
#              (2, '美国-旧金山'),
#              (3, '美国-休斯顿'),
#              (4, '美国-波士顿'),
#              (5, '美国-纽约'),
#              (6, '美国-芝加哥'),
#              (7, '美国-洛杉矶'),
#              (8, '美国-夏威夷'),
#              (9, '美国-其他城市'),
#             )),
#     )
#     name_intitute = models.CharField(verbose_name='邀请机构中文名称', max_length=100)
#     name_en_institute = models.CharField(verbose_name='邀请机构英文名称', max_length=100)
#     introduction = models.CharField(verbose_name='邀请机构简介', max_length=1000)
#     date_start = models.DateField(verbose_name='访问开始时间')
#     date_end = models.DateField(verbose_name='访问结束时间')
#     destination = models.IntegerField(verbose_name='请选择出访目的地', choices=destination_choices)
#     invitor = models.CharField(verbose_name='邀请人', max_length=50)
#     address_en = models.CharField(verbose_name='邀请单位地址', max_length=200)
#     tel = models.CharField(verbose_name='邀请人电话', max_length=12)
#     invitation_letter = models.FileField(verbose_name='邀请信', upload_to='upload/%Y/%m/')
#
