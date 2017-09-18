from django import forms
from rango.models import Page, Category, UserProfile
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

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    class Meta:
        model = User
        fields = ('username','email','password')
class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('website','picture')




    class Meta:
        model = Page
        exclude=('category',)


class ProjectForm(forms.ModelForm):
#    category = forms.ForeignKey(Category)
    title = forms.CharField(max_length = 128, help_text = "Please enter the title of the project in Chinese.")
    title_en = forms.CharField(max_length=200, help_text="Please enter the title of the project in English.")
#    url = forms.URLField(max_length = 200, help_text = "Please enter the URL of the page.")
    time_leave = forms.DateField(help_text = "Please enter the date of leaving.")
    time_back = forms.DateField(help_text="Please enter the date of come back.")
#    Members = forms.ManyToManyField(Personal_information,)
    Task_detail = forms.CharField(max_length=2000, help_text='任务内容以及意义描述')
    log = forms.CharField(max_length=2000, widget=forms.HiddenInput, help_text='进度记录')

    def clean(self):
        cleaned_data=self.cleaned_data
        url = cleaned_data.get('url')

        if url and not url.startswith('http://'):
            url = 'http://'+url
            cleaned_data['url']=url

            return cleaned_data


    class Meta:
        model = Page
        exclude=('Project',)