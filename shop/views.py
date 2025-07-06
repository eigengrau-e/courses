from django.http import HttpResponse
from django.shortcuts import render
from .models import Course


def index(request):
    courses = Course.objects.all()
    return HttpResponse(''.join([str(course) + "<br>" for course in courses]))
