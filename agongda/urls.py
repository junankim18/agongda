from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from .views import *

app_name = 'agongda'

urlpatterns = [
    path('', main, name='main'),
    path('signup', signup, name='signup'),
    path('login', login_view, name='login'),
    path('logout', logout, name='logout'),
    path('mypage', mypage, name='mypage'),
]
