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
    path('study/create', create_study, name='create_study'),
    path('study/apply/<int:pk>', apply, name='apply'),
    path('study/accept/<int:study_pk>/<int:user_pk>', accept, name='accept'),
    path('study/applicants/<int:pk>', applicants, name='applicants'),
    path('study/<int:pk>', study_detail, name='study_detail'),
    path('movetovalidation', movetovalidation, name='movetovalidation'),
    path('validation_verified', validation_verified, name='validation_verified'),
    path('validation', validation, name='validation'),

]
