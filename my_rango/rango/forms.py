from django import forms
from .choices import *
from .models import * #Page, Category, UserProfile
#from .models import PassportInformation, VisaInformation
from django.contrib.auth.models import User

class CategoryForm(forms.ModelForm):
    name = forms.CharField(max_length = 128,
                           help_text = "Please enter the category name.")
    views = forms.IntegerField(widget = forms.HiddenInput(), initial = 0)
    likes = forms.IntegerField(widget = forms.HiddenInput(), initial = 0)
    slug = forms.CharField(widget = forms.HiddenInput(), required=False)

    class Meta:
        model = Category
        fields = ('name',)

class PageForm(forms.ModelForm):
    title = forms.CharField(max_length = 128, help_text = "Please enter the title of the page.")
    url = forms.URLField(max_length = 200, help_text = "Please enter the URL of the page.")
    views = forms.IntegerField(widget = forms.HiddenInput, initial=0)
    likes = forms.IntegerField(widget=forms.HiddenInput, initial=0)

    def clean(self):
        cleaned_data=self.cleaned_data
        url = cleaned_data.get('url')

        if url and not url.startswith('http://'):
            url = 'http://'+url
            cleaned_data['url']=url

            return cleaned_data

    class Meta:
        model = Page
        exclude=('category',)


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username','email','password')
class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('website','picture')

#  我们自己的外事系统的forms
#


class PassportInformationForm(forms.ModelForm):
    # GENDER_CHOICES = (
    #     ('M', 'Male'),
    #     ('F', 'Female'),
    # )
    # PLACE_CHOICES = (
    #     ('SH', '上海市'),
    #     ('BJ', '北京市'),
    #     ('SD', '山东省'),
    #     ('HL', '黑龙江省'),
    #     ('JL', '吉林省'),
    #     ('LN', '辽宁省'),
    #     ('HB', '河北省'),
    #     ('NM', '内蒙古自治区'),
    #     ('TJ', '天津市'),
    #     ('SX', '山西省'),
    #     ('SH', '陕西省'),
    #     ('GS', '甘肃省'),
    #     ('XJ', '新疆维吾尔自治区'),
    #     ('QH', '青海省'),
    #     ('HE', '河南省'),
    #     ('NX', '宁夏回族自治区'),
    #     ('XZ', '西藏自治区'),
    #     ('SC', '四川省'),
    #     ('BH', '湖北省'),
    #     ('HU', '湖南省'),
    #     ('JS', '江苏省'),
    #     ('ZJ', '浙江省'),
    #     ('AH', '安徽省'),
    #     ('FJ', '福建省'),
    #     ('YN', '云南省'),
    #     ('GZ', '贵州省'),
    #     ('GD', '广东省'),
    #     ('GX', '广西壮族自治区'),
    #     ('CQ', '重庆市'),
    #     ('HA', '海南省'),
    #     ('JX', '江西省'),
    #     ('JW', '境外')
    # )
    name = forms.CharField(max_length = 10, )# help_text = "Please enter the name of the Passport.")
    birth_date = forms.DateField(label='出生日期')
    birth_place = forms.ChoiceField(label='出生地', choices=PLACE_CHOICES)
    gender = forms.ChoiceField(label='性别', choices=GENDER_CHOICES)
    Passport_number = forms.CharField(label='护照号码', max_length=15)
    date_issue = forms.DateField(label='颁发日期')
    date_expire = forms.DateField(label='过期日期')
    issue_office = forms.CharField(label='发证机关', max_length=15)
    issue_place = forms.CharField(label='发证地点', max_length=15)
    date_out = forms.DateField(label='借出日期')
    date_back = forms.DateField(label='归还日期')


class VisaInformationForm(forms.ModelForm):
    # visa_choices = (
    #     ('A', '一次入境签证'),
    #     ('B', '多次入境签证'),
    # )
    country = forms.CharField(label='国家', max_length=20)
    issue_date = forms.DateField(label='颁发日期')
    expire_date = forms.DateField(label='过期日期')
    visa_class = forms.ChoiceField(label='签证类型', choices=visa_choices)
    visa_file = forms.FileField(label='签证扫描件')
