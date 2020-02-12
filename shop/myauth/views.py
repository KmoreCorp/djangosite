from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from .forms import CustomerForm
from .models import NonVipUser
# Create your views here.

def index(request):
    return render(request, 'myauth/index.html')


def mylogin(request):
    if request.method == 'POST':
        user = authenticate(request, username= request.POST['username'], password = request.POST['password'])
        if user is None:
            return render(request, 'myauth/login.html',{'error':'用户名或密码错误，请重新输入。'})
        else:
            login(request, user)
            return redirect ('myauth:index')
    else:
        return render(request, 'myauth/login.html')

def mylogout(request):
    logout(request)
    return redirect ('myauth:index')

def register(request):
    if request.method == 'POST':
        regform = CustomerForm(request.POST)
        if regform.is_valid():
            regform.save()
            login_user = authenticate(username= regform.cleaned_data['username'], password = regform.cleaned_data['password1'])
            login(request, login_user)
            login_user.email = regform.save()
            NonVipUser(user = login_user, nickname=regform.cleaned_data['nickname'], birthday = regform.cleaned_data['birthday']).save()
            return redirect ('myauth:index')
    else:
        regform = CustomerForm()

    content = {'registerform': regform}
    return render(request, 'myauth/register.html', content)
