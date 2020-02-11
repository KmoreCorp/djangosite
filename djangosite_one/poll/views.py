from django.shortcuts import render, redirect

# Create your views here.
# from django.http import HttpResponse
from poll.models import Subject, Teacher, RegistrationForm, LoginForm, User #,Captcha



def show_subjects(request):
     """view on all subjects"""
     subjects = Subject.objects.all()
     return render(request, 'subject.html', {'subjects': subjects})

def show_teachers(request):
    """view on selected subject teachers"""
    try:
        sno = int(request.GET['sno'])
        subject = Subject.objects.get(no=sno)
        teachers = subject.teacher_set.all()
        return render(request, 'teachers.html', {'subject':subject, 'teachers':teachers})
    except (KeyError, ValueError, Subject.DoesNotExist):
        return redirect('/')

def prise_or_critisize(request):
    """Good"""
    try:
        tno = int(request.GET['tno'])
        teacher = Teacher.objects.get(no = tno)
        if request.path.startswith('/prise'):
            teacher.good_count += 1
        else:
            teacher.bad_count += 1
        teacher.save()
        data = {'code': 200, 'hint': 'Action Success'}
    except (KeyError, ValueError, Teacher.DoesNotExist):
        data = {'code': 404, 'hint': 'Action Failure'}
    return JsonResponse(data)

def register(request):
    page, hint = 'signup.html', ''
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            page = 'signin.html'
            hint = 'Success, please login'
        else:
            hint = 'Please enter valid registration infomation'
    return render(request, page, {'hint': hint})


def login(request):
    hint = ''
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = User.objects.filter(username=username, password=password).first()
            if user:
                return redirect('/')
            else:
                hint = '用户名或密码错误'
        else:
            hint = '请输入有效的登录信息'
    return render(request, 'signin.html', {'hint': hint})
