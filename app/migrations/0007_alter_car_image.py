# Generated by Django 5.0.4 on 2024-06-26 06:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_alter_car_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='image',
            field=models.FileField(blank=True, default=None, max_length=250, null=True, upload_to='images/'),
        ),
    ]
