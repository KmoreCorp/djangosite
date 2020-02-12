from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class NonVipUser(models.Model):
    """for Non VIP Users"""
    user = models.OneToOneField(User, on_delete = models.CASCADE)
    nickname = models.CharField(blank=True, max_length = 50, verbose_name='昵称')
    birthday = models.DateField(blank=True, verbose_name='生日')
    class Meta:
        verbose_name = '普通会员'
        verbose_name_plural = '普通会员'
