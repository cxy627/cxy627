from django import forms
from .models import Page,Category
from .models import User,UserProfile


class CategoryForm(forms.ModelForm):
    name = forms.CharField(max_length=128,
    help_text="请输入类型名字：")
    views =forms.IntegerField(widget=forms.HiddenInput(),initial=0)
    likes = forms.IntegerField(widget=forms.HiddenInput(),initial=0)
    slug = forms.CharField(widget=forms.HiddenInput(),initial=0)

    class Meta:
        model = Category
        fields = ("name",)

class PageForm(forms.ModelForm):
    title = forms.CharField(
        max_length=128,
        help_text="请输入页面标题："
        )
    url = forms.URLField(
        max_length=200,
        help_text="输入页面url："
        )
    views = forms.IntegerField(
        widget=forms.HiddenInput(),
        initial=0
    )
    class Meta:
        model=Page
        exclude=("category",)
    def clean(self):
        cleaned_data=self.cleaned_data
        url = cleaned_data.get("url")
        if url and not ((url.startswith("http://")) or (url.startswith("https://")) ):
            url = "http://"+ url
            cleaned_data["url"]=url
        print(cleaned_data)
        return cleaned_data

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username','email','password')

class UserProfileForm(forms.ModelForm):
    website  =  forms.URLField(required=False)
    picture  =  forms.ImageField(required=False)

    class Meta:
        model = UserProfile
        fields = ('website','picture')
