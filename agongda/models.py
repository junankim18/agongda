from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings


class CustomUser(AbstractUser):
    nickname = models.CharField(
        verbose_name='사용자 닉네임', max_length=100, unique=True)


class Study(models.Model):
    STUDY_CHOICES = (
        ('TOEIC', 'TOEIC'),
        ('TOEIC SPEAKING', 'TOEIC SPEAKING'),
        ('TOEFL', 'TOEFL'),
        ('OPIC', 'OPIC'),
        ('HSK', 'HSK'),
        ('JLPT', 'JLPT'),
    )
    STUDY_PLACE_CHOICES = (
        ('online', '온라인'),
        ('offline', '오프라인'),
    )

    study_name = models.CharField(verbose_name='스터디 이름', max_length=100)
    study_subject = models.CharField(
        choices=STUDY_CHOICES, max_length=50, default='TOEIC')
    study_limit = models.CharField(verbose_name='스터디 수준', max_length=100)
    study_people = models.IntegerField(verbose_name='스터디 인원수')
    study_place = models.CharField(
        choices=STUDY_PLACE_CHOICES, max_length=50, default='online')
    study_time = models.TextField(verbose_name='스터디 시간')
    study_detail = models.TextField(verbose_name='스터디 설명')
    study_applicants = models.ManyToManyField(CustomUser, related_name='study_applicants',
                                              verbose_name='스터디 지원자', blank=True)
    study_members = models.ManyToManyField(CustomUser, related_name='study_members',
                                           verbose_name='스터디 멤버', blank=True)
    study_leader = models.ForeignKey(
        CustomUser, related_name='study_leader', on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.study_name


class Validation(models.Model):
    opic = models.BooleanField(verbose_name='opic', default=False)
    opic_class = models.CharField(
        verbose_name='오픽 수준', max_length=100, blank=True, null=True)
    opic_validation = models.ImageField(
        upload_to='validations', blank=True, null=True)

    toeic = models.BooleanField(verbose_name='toeic', default=False)
    toeic_class = models.CharField(
        verbose_name='토익 수준', max_length=100, blank=True, null=True)
    toeic_validation = models.ImageField(
        upload_to='validations', blank=True, null=True)

    toefl = models.BooleanField(verbose_name='toefl', default=False)
    toefl_class = models.CharField(
        verbose_name='토플 수준', max_length=100, blank=True, null=True)
    toefl_validation = models.ImageField(
        upload_to='validations', blank=True, null=True)

    toeic_speaking = models.BooleanField(
        verbose_name='toeic speaking', default=False)
    toeic_speaking_class = models.CharField(
        verbose_name='토익 스피킹 수준', max_length=100, blank=True, null=True)
    toeic_speaking_validation = models.ImageField(
        upload_to='validations', blank=True, null=True)

    jlpt = models.BooleanField(verbose_name='JLPT', default=False)
    jlpt_class = models.CharField(
        verbose_name='JLPT 수준', max_length=100, blank=True, null=True)
    jlpt_validation = models.ImageField(
        upload_to='validations', blank=True, null=True)

    hsk = models.BooleanField(verbose_name='HSK', default=False)
    hsk_class = models.CharField(
        verbose_name='HSK 수준', max_length=100, blank=True, null=True)
    hsk_validation = models.ImageField(
        upload_to='validations', blank=True, null=True)


class Profile(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE
    )
    validations = models.ForeignKey(
        Validation, related_name='validations', verbose_name='인증 수준', on_delete=models.CASCADE, null=True, blank=True)
    studies = models.ManyToManyField(
        Study, related_name='studies', verbose_name='스터디', blank=True)
