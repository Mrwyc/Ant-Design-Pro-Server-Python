from django.db import models
import datetime

# Create your models here.

class UserModel(models.Model):
    username = models.CharField(verbose_name="用户名称", max_length=60)
    password = models.CharField(verbose_name="用户密码", max_length=80)
    user_token = models.CharField(verbose_name="用户凭证", max_length=80)
    register_time = models.DateTimeField(default=datetime.datetime.now())


class AriticeModel(models.Model):
    title = models.CharField(verbose_name="文章标题", max_length=150)
    aritice_user = models.CharField(verbose_name="文章作者", max_length=60)
    aritice_gjz = models.CharField(verbose_name='文章关键字', max_length=60)
    img_url = models.CharField(verbose_name='文章封面图', max_length=100)
    content = models.TextField(verbose_name="文章内容")
    create_time = models.DateTimeField(default=datetime.datetime.now(), verbose_name='文章创建时间')


class DirectoryModel(models.Model):
    directtory_name = models.CharField(verbose_name="一级目录", max_length=80)


class Directory_Secondary(models.Model):
    secondary_name = models.CharField(verbose_name='二级目录', max_length=100)
    directtore_id = models.ForeignKey('DirectoryModel', verbose_name='一级目录关系',  on_delete=models.CASCADE)


class Content_Directory(models.Model):
    directory_secondary_id = models.ForeignKey('Directory_Secondary', verbose_name='二级目录关系', on_delete=models.CASCADE)
    directory_content = models.TextField(verbose_name="话术内容")
    create_time = models.DateTimeField(default=datetime.datetime.now(), verbose_name="发布时间")
