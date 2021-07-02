from django.contrib.auth.forms import UserCreationForm
from .models import *
from django import forms


class RegisterForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'password1', 'password2', 'nickname']


class ValidationForm(forms.Form):
    opic_class = forms.CharField(
        label='오픽 수준', max_length=100)
    opic_validation = forms.ImageField()

    toeic_class = forms.CharField(
        label='토익 수준', max_length=100)
    toeic_validation = forms.ImageField()

    toefl_class = forms.CharField(
        label='토플 수준', max_length=100)
    toefl_validation = forms.ImageField()

    toeic_speaking_class = forms.CharField(
        label='토익 스피킹 수준', max_length=100)
    toeic_speaking_validation = forms.ImageField()

    jlpt_class = forms.CharField(
        label='JLPT 수준', max_length=100)
    jlpt_validation = forms.ImageField()

    hsk_class = forms.CharField(
        label='HSK 수준', max_length=100)
    hsk_validation = forms.ImageField()
