# Generated by Django 5.0.6 on 2024-06-29 06:51

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0010_alter_profile_user'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='email',
        ),
        migrations.RemoveField(
            model_name='book',
            name='image',
        ),
        migrations.RemoveField(
            model_name='book',
            name='image1',
        ),
        migrations.AddField(
            model_name='book',
            name='file',
            field=models.FileField(blank=True, default=None, max_length=250, null=True, upload_to='imgs/'),
        ),
        migrations.AddField(
            model_name='book',
            name='img',
            field=models.FileField(blank=True, default=None, max_length=250, null=True, upload_to='img/'),
        ),
        migrations.AddField(
            model_name='book',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]