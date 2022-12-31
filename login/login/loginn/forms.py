from django import forms

from django.contrib.auth.models import User
from django.core import validators

def username_val(value):
    if User.objects.filter(username=value).exists():
        raise forms.ValidationError("username already exixts")

def email_val(value):
    if User.objects.filter(email=value).exists():
        raise forms.ValidationError("email already exixts")


class loginform(forms.Form):
    email=forms.EmailField()
    password=forms.CharField(widget=forms.PasswordInput())

    def clean(self):
        cleaned_data=super().clean()
        if self.is_valid():
            email=self.cleaned_data['email']
            if not User.objects.filter(email=email).exists():
                raise forms.ValidationError("email or username incorrect")


class signupform(forms.Form):
    username=forms.CharField(validators=[username_val])
    email=forms.EmailField(validators=[email_val])
    password=forms.CharField(widget=forms.PasswordInput())


    