from django.shortcuts import render

# Create your views here.
# from django.http import HttpResponse
from poll.models import Subject, Teacher

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
