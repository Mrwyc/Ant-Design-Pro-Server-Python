from django.db import models
import datetime

# Create your models here.

class UserModel(models.Model):
    username = models.CharField(verbose_name="用户名称", max_length=60)
    password = models.CharField(verbose_name="用户密码", max_length=80)
    user_token = models.CharField(verbose_name="用户凭证", max_length=80)
    register_time = models.DateTimeField(default=datetime.datetime.now())
