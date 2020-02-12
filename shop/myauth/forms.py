from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

class CustomerForm(UserCreationForm):
    """docstring for CustomerForm."""
    nickname = forms.CharField(max_length=50, required=False, label ='昵称')
    birthday = forms.DateField(required=False, label='生日')

    class Meta:
        model = User
        fields = ('username', 'password1','password2','email','nickname','birthday')
