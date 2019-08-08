# Generated by Django 2.1.3 on 2019-08-07 14:17

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('User', '0003_auto_20190807_1050'),
    ]

    operations = [
        migrations.CreateModel(
            name='Setting_Web',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('xitong_name', models.CharField(max_length=200, verbose_name='系统名称')),
            ],
        ),
        migrations.AlterField(
            model_name='ariticemodel',
            name='create_time',
            field=models.DateTimeField(default=datetime.datetime(2019, 8, 7, 14, 17, 54, 637794), verbose_name='文章创建时间'),
        ),
        migrations.AlterField(
            model_name='content_directory',
            name='create_time',
            field=models.DateTimeField(default=datetime.datetime(2019, 8, 7, 14, 17, 54, 639789), verbose_name='发布时间'),
        ),
        migrations.AlterField(
            model_name='usermodel',
            name='register_time',
            field=models.DateTimeField(default=datetime.datetime(2019, 8, 7, 14, 17, 54, 636797)),
        ),
    ]