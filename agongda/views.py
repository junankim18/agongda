from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import authenticate, login, logout
from .forms import *
from .models import *
from django.http import HttpResponseRedirect
from django.contrib import auth


def main(request):
    studies = Study.objects.all()
    ctx = {
        'studies': studies
    }
    return render(request, 'main.html', ctx)


def signup(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            new_validations = Validation()
            new_validations.save()
            new_profile = Profile()
            new_profile.user = user
            new_profile.validations = new_validations
            new_profile.save()
            login(request, user)
            return redirect('/')

        else:
            form = RegisterForm()
            ctx = {
                'form': form,
                'error': 'username or password is incorrect'
            }
            return render(request, 'signup.html', ctx)

    else:
        form = RegisterForm()
        ctx = {
            'form': form
        }
        return render(request, 'signup.html', ctx)


def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request=request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(
                request=request, username=username, password=password)
            if user is not None:
                login(request, user)
            return redirect('/')
        else:
            form = AuthenticationForm()
            ctx = {
                'form': form,
                'error': 'username or password is incorrect'
            }
            return render(request, 'login.html', ctx)

    elif request.method == 'GET':
        form = AuthenticationForm()
        ctx = {
            'form': form
        }
        return render(request, 'login.html', ctx)


def logout(request):
    auth.logout(request)
    return HttpResponseRedirect('/')


def mypage(request):
    user = request.user
    profile = Profile.objects.get(user=user)
    validform = ValidationForm()
    test_list = [profile.validations.opic, profile.validations.opic_class, profile.validations.opic_validation,
                 profile.validations.toeic, profile.validations.toeic_class, profile.validations.toeic_validation,
                 profile.validations.toefl, profile.validations.toefl_class, profile.validations.toefl_validation,
                 profile.validations.toeic_speaking, profile.validations.toeic_speaking_class, profile.validations.toeic_speaking_validation,
                 profile.validations.jlpt, profile.validations.jlpt_class, profile.validations.jlpt_validation,
                 profile.validations.hsk, profile.validations.hsk_class, profile.validations.hsk_validation, ]
    if request.method == 'GET':
        ctx = {
            'profile': profile,
            'validform': validform
        }
        return render(request, 'mypage.html', ctx)
    elif request.method == 'POST':

        new_validation = profile.validations

        test = request.POST['test']
        if test == 'opic':
            new_validation.opic_class = request.POST['class']
            new_validation.opic_validation = request.FILES['image']
        elif test == 'toeic':
            new_validation.toeic_class = request.POST['class']
            new_validation.toeic_validation = request.FILES['image']
        elif test == 'toefl':
            new_validation.toefl_class = request.POST['class']
            new_validation.toefl_validation = request.FILES['image']
        elif test == 'toeic_speaking':
            new_validation.toeic_speaking_class = request.POST['class']
            new_validation.toeic_speaking_validation = request.FILES['image']
        elif test == 'jlpt':
            new_validation.jlpt_speaking_class = request.POST['class']
            new_validation.jlpt_speaking_validation = request.FILES['image']
        elif test == 'hsk':
            new_validation.hsk_speaking_class = request.POST['class']
            new_validation.hsk_speaking_validation = request.FILES['image']
        new_validation.save()

        ctx = {
            'profile': profile,
            'test_list': test_list
        }

        return render(request, 'mypage.html', ctx)
