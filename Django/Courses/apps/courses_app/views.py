# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse, redirect
from . import models


# Create your views here.
def index(request):
    getcourses = models.Courses.objects.all()
    print getcourses
    context = {
        'courses': getcourses,
    }
    return render(request, "index.html", context)

def add(request):
    print request.POST
    course_name = request.POST['name']
    course_description = request.POST['description']
    models.Courses.objects.create(name=course_name,  description=course_description)
    return redirect('/')

def edit(request, course_id):
    getcourses = models.Courses.objects.get(id=course_id)
    context = {
        'id': course_id,
        'course': getcourses,
    }
    return render(request, "edit.html", context)

def destroy(request, course_id):
    getcourses = models.Courses.objects.get(id=course_id)
    getcourses.delete()
    return redirect('/')