# Generated by Django 5.0.6 on 2024-06-29 08:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0013_remove_book_image_book_img'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='img',
        ),
    ]
