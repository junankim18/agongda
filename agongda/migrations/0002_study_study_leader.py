# Generated by Django 3.2.5 on 2021-07-03 04:40

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('agongda', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='study',
            name='study_leader',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='study_leader', to=settings.AUTH_USER_MODEL),
        ),
    ]
