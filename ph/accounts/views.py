from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth
# Create your views here.

# app_name = 'accounts'


def signup(request):
	if request.method == 'GET':
		return render(request, 'signup.html')
	elif request.method == 'POST':
		user_name = request.POST['username']
		password1 = request.POST['password1']
		password2 = request.POST['password2']
		try:
			User.objects.get(username=user_name)
			return render(request, 'signup.html', {'username_error': '用户已经存在'})
		except User.DoesNotExist:
			if password1 == password2:
				User.objects.create_user(username=user_name, password = password1)
				return redirect ('products:product_page')
			else:
				return render(request, 'signup.html', {'password_error': '两次输入的密码不一致'})

def login(request):
	if request.method == 'GET':
		return render(request, 'login.html')
	elif request.method == 'POST':
		user_name = request.POST['username']
		password = request.POST['password']
		user = auth.authenticate(username=user_name, password=password)
		if user is None:
			return render(request, 'login.html', {'login_error': '用户名或密码错误'})
		else:
			auth.login(request, user)
			return redirect ('products:product_page')
def logout(request):
	if request.method == 'POST':
		auth.logout(request)
		return redirect ('products:product_page')