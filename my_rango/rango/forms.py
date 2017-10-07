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

class PersonalInfromationForm(forms.ModelForm):
    name = forms.CharField(label='姓名', max_length=10)
    tel = forms.CharField(label='电话', max_length=12)
    email = forms.EmailField()
    gender = forms.ChoiceField(label='性别', choices=GENDER_CHOICES)
    department = forms.CharField(label='所在部门', max_length=30)
    ID_num = forms.CharField(label='18位身份证号', max_length=18)
    Place_of_Birth = forms.ChoiceField(label='出生地（省）', choices=PLACE_CHOICES)
    Date_of_Birth = forms.DateField(label='出生日期')
    duty = forms.ChoiceField(label='职务', choices=duty_choices)
    identity = forms.ChoiceField(label='对外身份', choices=identity_choices)
    race = forms.ChoiceField(label='民族', choices=race_choices)
    political_identity = forms.ChoiceField(label='政治面貌', choices=political_choices)
    securety = forms.ChoiceField(label='涉密等级', choices=securety_choices)
    status_health = forms.ChoiceField(label='健康状况', choices=health_choices)
    emergency_contact_name = forms.CharField(label='紧急联系人姓名', max_length=10)
    emergency_contact_tel = forms.CharField(label='紧急联系人电话', max_length=11)


class PassportInformationForm(forms.ModelForm):
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
