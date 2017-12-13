# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse, redirect 

# Create your views here.


def index(request):
    return render(request, "index.html")


def process(request):
    if request.method == 'POST':
        if not 'count' in request.session:
            request.session['count'] = 1
        else:
            request.session['count'] += 1
        data = request.POST
        request.session['name'] = data.get('name')
        request.session['location'] = data.get('location')
        request.session['lang'] = data.get('lang')
        request.session['comment'] = data.get('comments')
    return redirect('/results')


def results(request):
    context = {
        "count": request.session['count'],
        "name": request.session['name'],
        "location": request.session['location'],
        "lang": request.session['lang'],
        "comment": request.session['comment'],
    }
    return render(request, "index2.html", context)
