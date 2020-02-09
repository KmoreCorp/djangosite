from django.shortcuts import render

# Create your views here.
# from django.http import HttpResponse
from poll.models import Subject, Teacher

def show_subjects(request):
     """view on all subjects"""
     subjects = Subject.objects.all()
     return render(request, 'subject.html', {'subjects': subjects})