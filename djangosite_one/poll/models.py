from django.db import models
from django import forms
import re
import hashlib

#for captcha
import os
import random

from io import BytesIO

from PIL import Image
from PIL import ImageFilter
from PIL.ImageDraw import Draw
from PIL.ImageFont import truetype
#-----#

# Create your models here.
class Subject(models.Model):
    """Subjects"""
    no = models.IntegerField(primary_key = True, verbose_name = 'No.')
    name = models.CharField(max_length =20, verbose_name = 'Name')
    intro = models.CharField(max_length = 511, verbose_name = 'Introduction', default ='')
    create_date = models.DateField(null=True, verbose_name ='Date of Creation')
    is_hot = models.BooleanField(default=False, verbose_name = 'Popularity')

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'tb_subject'
        verbose_name = 'Subject'
        verbose_name_plural = 'Subjects'

class Teacher(models.Model):
    """Teacher"""
    no = models.IntegerField(primary_key =True, verbose_name ='No.')
    name = models.CharField(max_length = 20, verbose_name = 'Name')
    detail = models.CharField(max_length=1023, default ='', blank = True, verbose_name='Details')
    photo = models.CharField(max_length=1023, default='', verbose_name = 'Photo')
    good_count = models.IntegerField(default=0, verbose_name='Good No.')
    bad_count = models.IntegerField(default=0, verbose_name ='Bad No.')
    subject = models.ForeignKey(Subject, on_delete = models.PROTECT, verbose_name='Belongs to')

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'tb_teacher'
        verbose_name = 'Teacher'
        verbose_name_plural = 'Teachers'

class User(models.Model):
    """Users"""
    no = models.AutoField(primary_key=True, verbose_name='No.')
    username = models.CharField(max_length = 20, unique=True, verbose_name='Username')
    password = models.CharField(max_length=32, verbose_name='Password')
    regdate = models.DateTimeField(auto_now_add=True, verbose_name='Registration Time')

    class Meta:
        db_table = 'tb_user'
        verbose_name_plural = 'Users'

USERNAME_PATTERN = re.compile (r'\w{4,20}')
def to_md5_hex(message):
    return hashlib.md5(message.encode()).hexdigest()

class RegistrationForm(forms.ModelForm):
    repassword = forms.CharField(min_length = 4, max_length = 20)

    def clean_username(self):
        username = self.cleaned_data['username']
        if not USERNAME_PATTERN.fullmatch(username):
            raise ValidationError('Username contains number(0-9), alphabeta(a-z,A-Z) and dash only, must between 4 characters 20.')
        return username
    def clean_password(self):
        password = self.cleaned_data['password']
        if len(password) < 8 or len(password)>20 :
            raise ValidationError('Invalid, Passwords must between 8 characters 20')
        return to_md5_hex(self.cleaned_data['password'])

    def clean_repassword(self):
        repassword = to_md5_hex(self.cleaned_data['repassword'])
        if repassword != self.cleaned_data['password']:
            raise ValidationError('Please Confirm agian with password')
        return repassword

    class Meta:
        model = User
        exclude = ('no', 'regdate')

class LoginForm(forms.Form):
    username = forms.CharField(min_length=4, max_length=20)
    password = forms.CharField(min_length=8, max_length=20)
    #  captcha = forms.CharField(min_length=4, max_length=4)

    def clean_username(self):
        username = self.cleaned_data['username']
        if not USERNAME_PATTERN.fullmatch(username):
            raise ValidationError('无效的用户名')
        return username

    def clean_password(self):
        return to_md5_hex(self.cleaned_data['password'])
