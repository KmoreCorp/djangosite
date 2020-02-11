from django.shortcuts import render, redirect

# Create your views here.
from django.http import HttpResponse, JsonResponse
from poll.models import Subject, Teacher, RegistrationForm, LoginForm, User
import xlwt
from urllib.parse import quote
from io import BytesIO
#,Captcha



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
    """login"""
    hint = ''
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = User.objects.filter(username=username, password=password).first()
            if user:
                # 登录成功后将用户编号和用户名保存在session中
                request.session['userid'] = user.no
                request.session['username'] = user.username
                return redirect('/')
            else:
                hint = '用户名或密码错误'
        else:
            hint = '请输入有效的登录信息'
    return render(request, 'signin.html', {'hint': hint})

def logout(request):
    """注销"""
    request.session.flush()
    return redirect('/')

def export_teachers_excel(request):
    # 创建工作簿
    wb = xlwt.Workbook()
    # 添加工作表
    sheet = wb.add_sheet('老师信息表')
    # 查询所有老师的信息(注意：这个地方稍后需要优化)
    queryset = Teacher.objects.all()
    # 向Excel表单中写入表头
    colnames = ('姓名', '介绍', '好评数', '差评数', '学科')
    for index, name in enumerate(colnames):
        sheet.write(0, index, name)
    # 向单元格中写入老师的数据
    props = ('name', 'detail', 'good_count', 'bad_count', 'subject')
    for row, teacher in enumerate(queryset):
        for col, prop in enumerate(props):
            value = getattr(teacher, prop, '')
            if isinstance(value, Subject):
                value = value.name
            sheet.write(row + 1, col, value)
    # 保存Excel
    buffer = BytesIO()
    wb.save(buffer)
    # 将二进制数据写入响应的消息体中并设置MIME类型
    resp = HttpResponse(buffer.getvalue(), content_type='application/vnd.ms-excel')
    # 中文文件名需要处理成百分号编码
    filename = quote('老师.xls')
    # 通过响应头告知浏览器下载该文件以及对应的文件名
    resp['content-disposition'] = f'attachment; filename="{filename}"'
    return resp

def get_teachers_data(request):
    # 查询所有老师的信息(注意：这个地方稍后也需要优化)
    queryset = Teacher.objects.all()
    # 用生成式将老师的名字放在一个列表中
    names = [teacher.name for teacher in queryset]
    # 用生成式将老师的好评数放在一个列表中
    good = [teacher.good_count for teacher in queryset]
    # 用生成式将老师的差评数放在一个列表中
    bad = [teacher.bad_count for teacher in queryset]
    # 返回JSON格式的数据
    return JsonResponse({'names': names, 'good': good, 'bad': bad})
