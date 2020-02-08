from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


depts_list = [
    {'no': 10, 'name': 'Finance Dept', 'location': 'Beijing'},
    {'no': 20, 'name': 'R&D Dept', 'location': 'Shenzhen'},
    {'no': 30, 'name': 'Saels Dept', 'location': 'Shanghai'},
]


def index(request):
    #  return HttpResponse('<h1>Hello, Django! This is a HR system.</h1>')
    return render(request, 'index.html', {'depts_list': depts_list})
