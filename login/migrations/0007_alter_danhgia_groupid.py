# Generated by Django 5.0.6 on 2024-05-27 11:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0006_user_fullname'),
    ]

    operations = [
        migrations.AlterField(
            model_name='danhgia',
            name='groupid',
            field=models.IntegerField(),
        ),
    ]
