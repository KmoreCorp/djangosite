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
